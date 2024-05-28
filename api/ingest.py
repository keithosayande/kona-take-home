from fastapi import UploadFile
from llama_index.core import StorageContext, SimpleDirectoryReader, Settings, VectorStoreIndex
import tempfile
import os
from llama_index.core.extractors import (
    TitleExtractor,
    QuestionsAnsweredExtractor,
    TitleExtractor,
    KeywordExtractor,
    BaseExtractor,
    SummaryExtractor,

)
from llama_index.extractors.entity import EntityExtractor
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.llms.openai import OpenAI
from llama_index.storage.docstore.mongodb import MongoDocumentStore
from llama_index.storage.index_store.mongodb import MongoIndexStore
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from api.db_client import get_mongo_client
os.environ["OPENAI_API_KEY"]

async def run_ingest(file: UploadFile):
    llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo", max_tokens=512)
    mongo_uri = os.getenv("MONGODB_URI")
    if not mongo_uri:
        print("MONGODB_URI not set in environment variables")
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = os.path.join(temp_dir, file.filename)
            # Save the uploaded file to the temporary directory
            with open(temp_file_path, 'wb') as temp_file:
                content = await file.read()
                temp_file.write(content)
            documents = SimpleDirectoryReader(input_files=[temp_file_path], filename_as_id=True).load_data()
            
            client = get_mongo_client()
            
            vector_store = MongoDBAtlasVectorSearch(client=client, db_name="kona_take_home", collection_name="documents")
            storage_context = StorageContext.from_defaults(
                docstore=MongoDocumentStore.from_uri(uri=mongo_uri, db_name="kona_take_home", namespace="documents"),
                index_store=MongoIndexStore.from_uri(uri=mongo_uri),
            )
            print(f"Connected to MongoDB Atlas Vector Store: {vector_store}")
            pipeline =IngestionPipeline(
                transformations=[
                    TitleExtractor(nodes=5, llm=llm),
                    QuestionsAnsweredExtractor(questions=3, llm=llm),
                    SummaryExtractor(summaries=["prev", "self"], llm=llm),
                    KeywordExtractor(keywords=5, llm=llm),
                ],
            )
            nodes = await pipeline.arun(documents=documents)
            storage_context.docstore.add_documents(nodes)
    
    except ValueError as e:
       raise e
    return {"message": "Ingested successfully"}
            
