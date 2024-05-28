from fastapi import FastAPI, UploadFile, File, HTTPException
import tempfile
import os
import shutil
import json
from api.ingest import run_ingest
from api.fetch import get_all
app = FastAPI()


@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        data = await run_ingest(file)
    except ValueError as e:
        raise HTTPException(status_code=418, detail=str(e))

    if isinstance(data, (str, bytes, bytearray)):
        data = json.loads(data)

    return {"message": data}

@app.get("/api/documents")
async def get_documents():
    try:
        data = await get_all()
    except ValueError as e:
        raise HTTPException(status_code=418, detail=str(e))

    if isinstance(data, (str, bytes, bytearray)):
        data = json.loads(data)

    return {"message": data}