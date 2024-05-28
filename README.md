<p align="center">
    <h1 align="center">KONA-TAKE-HOME</h1>
</p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=default&logo=tqdm&logoColor=black" alt="tqdm">
	<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=default&logo=JavaScript&logoColor=black" alt="JavaScript">
	<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=default&logo=scikit-learn&logoColor=white" alt="scikitlearn">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=default&logo=Pydantic&logoColor=white" alt="Pydantic">
	<img src="https://img.shields.io/badge/PostCSS-DD3A0A.svg?style=default&logo=PostCSS&logoColor=white" alt="PostCSS">
	<img src="https://img.shields.io/badge/Autoprefixer-DD3735.svg?style=default&logo=Autoprefixer&logoColor=white" alt="Autoprefixer">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=default&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style=default&logo=SciPy&logoColor=white" alt="SciPy">
	<img src="https://img.shields.io/badge/React-61DAFB.svg?style=default&logo=React&logoColor=black" alt="React">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=default&logo=Poetry&logoColor=white" alt="Poetry">
	<img src="https://img.shields.io/badge/ESLint-4B32C3.svg?style=default&logo=ESLint&logoColor=white" alt="ESLint">
	<br>
	<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=default&logo=OpenAI&logoColor=white" alt="OpenAI">
	<img src="https://img.shields.io/badge/SemVer-3F4551.svg?style=default&logo=SemVer&logoColor=white" alt="SemVer">
	<img src="https://img.shields.io/badge/SymPy-3B5526.svg?style=default&logo=SymPy&logoColor=white" alt="SymPy">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=default&logo=TypeScript&logoColor=white" alt="TypeScript">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=default&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Ajv-23C8D2.svg?style=default&logo=Ajv&logoColor=white" alt="Ajv">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=default&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=default&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=default&logo=FastAPI&logoColor=white" alt="FastAPI">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=default&logo=JSON&logoColor=white" alt="JSON">
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

The kona-take-home project integrates Next.js frontend with a FastAPI backend to enable document upload, retrieval, and processing. I know the brief said to just have a text area, but  I wanted to challenege myself, so I went with file uploads instead. I used [LlamaIndex](https://docs.llamaindex.ai/en/stable/) to orchestrate file ingestion -> file parsing -> automated metadata extraction(using OpenAI) -> storing in a Mongodb Database. Currently I couldn't find the limit in file size.  Documents that are multiple pages are split in to sepearate databse entries.


My thought process was that the Take Home Prompt and what Kona does is atleast partially [Retrieval augmented generation(RAG)](https://www.superannotate.com/blog/rag-explained), so by using LlamaIndex and Mongodb, this example project could be expanded to store embeddings within the documents and create a vector index combined with the metadata, would allow for relevant context documents to be retrieved quickly.


---

##  Repository Structure

```sh
└── kona-take-home/
    ├── LICENSE
    ├── README.md
    ├── api
    │   ├── __init__.py
    │   ├── db_client.py
    │   ├── fetch.py
    │   ├── index.py
    │   └── ingest.py
    ├── app
    │   ├── favicon.ico
    │   ├── globals.css
    │   ├── layout.tsx
    │   └── page.tsx
    ├── next.config.js
    ├── package-lock.json
    ├── package.json
    ├── poetry.lock
    ├── postcss.config.js
    ├── public
    │   ├── next.svg
    │   └── vercel.svg
    ├── pyproject.toml
    ├── requirements.txt
    ├── tailwind.config.js
    ├── tsconfig.json
    └── yarn.lock
```

---

##  Modules

<details closed><summary>.</summary>

| File                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [tailwind.config.js](tailwind.config.js) | Defines Tailwind CSS configurations for pages, components, and app files in the project. Extends theme with custom background images.                                                                                                                                                                                                                                                                                        |
| [requirements.txt](requirements.txt)     | Defines dependencies for enhanced functionality, including accelerators, web interaction, data processing, and AI capabilities. Ensures seamless integration with project structure for robust, scalable performance.                                                                                                                                                                                                        |
| [pyproject.toml](pyproject.toml)         | Defines dependencies for the API project, including FastAPI, Uvicorn, motor, and pymongo, essential for building and running the API server. The file also specifies additional libraries for data extraction, storage, and vector stores.                                                                                                                                                                                   |
| [next.config.js](next.config.js)         | Configures API rewrites for local and production environments based on NODE_ENV.                                                                                                                                                                                                                                                                                                                                             |
| [package-lock.json](package-lock.json)   | Fetch.py`The `fetch.py` file in the `api` directory of the repository is responsible for handling data fetching operations. It facilitates the retrieval of external resources and data required for the applications functionality. This component plays a crucial role in ensuring that the application has access to up-to-date and relevant information by making efficient requests and handling responses effectively. |
| [package.json](package.json)             | Enables development and deployment workflows for Next.js and FastAPI integration. Facilitates running development servers concurrently. Manages build processes and linting. Handles dependencies for enhanced frontend and backend capabilities.                                                                                                                                                                            |
| [tsconfig.json](tsconfig.json)           | Defines TypeScript configuration for Next.js app, targeting ES5, supporting JSX, and leveraging modules. Ensures strict type-checking and enforces consistent file casing. Enables JSON resolution, isolated modules, and allows JS files. Integrates Next.js plugin and custom path aliasing for cleaner imports.                                                                                                           |
| [postcss.config.js](postcss.config.js)   | Optimize Tailwind CSS and autoprefix stylesheets to enhance website styling in the projects frontend architecture.                                                                                                                                                                                                                                                                                                           |

</details>

<details closed><summary>app</summary>

| File                           | Summary                                                                                                                                                                                                              |
| ---                            | ---                                                                                                                                                                                                                  |
| [layout.tsx](app/layout.tsx)   | Defines RootLayout for app, configures metadata, and includes global styles. Maintains consistent font across app pages. Improves user experience and brand consistency.                                             |
| [page.tsx](app/page.tsx)       | Enables document upload functionality using FilePond in the apps Home page. Supports single file upload with a drag-and-drop interface. Integrated with the /api/upload' server endpoint for seamless file handling. |
| [globals.css](app/globals.css) | Defines global styles using Tailwind CSS for consistent appearance across the web application. Provides base, components, and utility classes. Influences overall design consistency and styling coherence.          |

</details>

<details closed><summary>api</summary>

| File                             | Summary                                                                                                                                                                                                                                      |
| ---                              | ---                                                                                                                                                                                                                                          |
| [fetch.py](api/fetch.py)         | Retrieves all documents from the specified MongoDB collection using a client object.                                                                                                                                                         |
| [ingest.py](api/ingest.py)       | Ingests and processes uploaded files by extracting key information using OpenAI and MongoDB databases, enhancing the search capabilities of the overall system.                                                                              |
| [index.py](api/index.py)         | Handles file upload and document retrieval in the FastAPI-based backend. Processes uploaded files and retrieves documents, ensuring data integrity.                                                                                          |
| [db_client.py](api/db_client.py) | Establishes a MongoDB client connection using the specified URI, ensuring adherence to API versioning and deprecation rules. Centralizes database access configuration for consistent and reliable data interaction within the API services. |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version 3.12`

###  Installation

> 1. Clone the kona-take-home repository:
>
> ```console
> $ git clone https://github.com/keithosayande/kona-take-home.git
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd kona-take-home
> ```
>
> 3. Install the dependencies:
> ```console
> $ yarn install
> ```

###  Usage


> Run kona-take-home using the command below:
> ```console
> $ yarn dev
> ```

