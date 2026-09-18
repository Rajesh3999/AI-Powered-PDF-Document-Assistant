# AI-Powered PDF Document Assistant

A beginner-friendly **Retrieval-Augmented Generation (RAG)** application that lets users upload a PDF and ask questions about its content.

The application extracts text from the PDF, splits it into smaller chunks, converts the chunks into embeddings, indexes them with **FAISS**, retrieves relevant content for a user's question, and uses an **OpenAI GPT model** to generate an answer from the retrieved context.

## Features

- Upload PDF documents through a Streamlit interface
- Extract text page-by-page using PyPDF
- Preserve page numbers as source metadata
- Split document text into smaller chunks
- Generate embeddings for document chunks
- Build an in-memory FAISS vector index
- Perform similarity-based retrieval
- Generate answers using retrieved document context and OpenAI GPT
- Display source page numbers with answers
- Maintain chat history during the current session
- Clear chat history
- Validate the OpenAI API key
- Handle empty or unreadable PDFs with user-friendly errors

## How It Works

```text
PDF
 ↓
Text Extraction
 ↓
Text Chunking
 ↓
Embeddings
 ↓
FAISS Vector Index
 ↓
User Question
 ↓
Question Embedding
 ↓
Similarity Search
 ↓
Relevant Chunks
 ↓
Context + Question
 ↓
OpenAI GPT
 ↓
Answer + Source Pages
```

### RAG Pipeline

**RAG (Retrieval-Augmented Generation)** first retrieves relevant information from the uploaded document and then provides that information as context to the language model.

This project follows:

1. Extract text from the PDF.
2. Split the text into smaller chunks.
3. Generate embeddings for the chunks.
4. Store/index embeddings using FAISS.
5. Convert the user's question into an embedding.
6. Search FAISS for similar document chunks.
7. Use the retrieved chunks as context.
8. Send the context and question to GPT.
9. Display the generated answer and source pages.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application interface |
| OpenAI API | Embeddings and GPT-based answer generation |
| LangChain | Text-splitting utilities |
| FAISS | Vector indexing and similarity search |
| PyPDF | PDF text extraction |
| python-dotenv | Environment variable management |
| NumPy | Numerical/vector operations |

## Project Structure

```text
AI-Powered-PDF-Document-Assistant/
│
├── app.py
│
├── src/
│   ├── pdf_processor.py
│   ├── utils.py
│   ├── embeddings.py
│   └── rag_pipeline.py
│
├── data/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### Main Files

- **`app.py`** — Streamlit UI, PDF upload, session state, indexing, questions, answers, and chat history.
- **`src/pdf_processor.py`** — Extracts text from PDF pages.
- **`src/utils.py`** — Splits extracted text into chunks.
- **`src/embeddings.py`** — Creates text embeddings.
- **`src/rag_pipeline.py`** — Handles FAISS indexing, retrieval, context construction, and answer generation.
- **`requirements.txt`** — Lists required Python packages.
- **`.env`** — Stores the OpenAI API key locally.
- **`.gitignore`** — Prevents secrets and generated/local files from being committed.

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI-Powered-PDF-Document-Assistant
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scriptsctivate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the OpenAI API Key

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

**Never commit your real API key to GitHub.**

Make sure `.env` is included in `.gitignore`.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## Example Questions

After uploading a PDF, try questions such as:

```text
What is the main purpose of this document?
```

```text
What are the key findings?
```

```text
What limitations are mentioned?
```

```text
Which page discusses the conclusion?
```

```text
What are the main challenges described?
```

## Example User Flow

```text
1. Open the application
2. Upload a PDF
3. Wait for the document to be indexed
4. Enter a question
5. The application searches the document
6. Relevant chunks are retrieved
7. GPT generates the answer
8. Source page numbers are displayed
```

## Why RAG?

A large document may contain much more information than is relevant to a particular question. Instead of sending the entire document to the language model for every question, the application retrieves relevant chunks first.

This helps the model focus on information related to the user's question and provides document-grounded context.

## Embeddings and FAISS

### Embeddings

An embedding converts text into a numerical vector representation that can be used to compare semantic similarity.

```text
Text
 ↓
Embedding Model
 ↓
Vector
```

### FAISS

FAISS is used to index and search these vectors efficiently.

```text
Document Chunks
 ↓
Embeddings
 ↓
FAISS Index
 ↓
Similarity Search
```

The user's question is also converted into an embedding, and FAISS is searched for the most relevant document chunks.

## Security

The OpenAI API key is loaded from an environment variable rather than being hard-coded in the source code.

Do **not**:

```python
OPENAI_API_KEY = "sk-..."
```

Instead, use:

```env
OPENAI_API_KEY=your_api_key_here
```

and load it through `python-dotenv`.

Before pushing to GitHub, verify that `.env` is ignored:

```bash
git status
```

If a real API key was ever committed to Git, rotate/revoke that key immediately.

## Error Handling

The application includes basic handling for:

- Missing OpenAI API key
- Invalid or unreadable PDF
- PDF with no extractable text
- Asking a question before a PDF is indexed
- Errors during document processing
- Errors during question answering

## Limitations

This is a learning/demo application and is not currently designed as a production-scale document platform.

Current limitations:

- FAISS index is in memory
- Index is not persisted between application sessions
- No user authentication
- No persistent database
- No rate limiting
- Single-document/session-oriented workflow
- Retrieval quality depends on chunking and embedding quality
- Application depends on OpenAI API availability and quota

## Future Improvements

Possible improvements include:

- Persist FAISS indexes to disk
- Use a managed vector database for production workloads
- Support multiple documents
- Add document management
- Add user authentication
- Store chat history in a database
- Improve source citations
- Add retrieval and answer evaluation
- Add logging and monitoring
- Add rate limiting and usage controls
- Improve chunking and retrieval strategies
- Support larger documents efficiently

## Learning Objectives

This project provides practical exposure to:

- Python application development
- PDF processing
- Text extraction
- Text chunking
- Embeddings
- Vector representations
- Semantic search
- FAISS
- Retrieval-Augmented Generation
- Large Language Models
- Prompt engineering
- OpenAI API integration
- Streamlit
- Environment-variable based secret management

## Project Summary

> This project is a RAG-based PDF question-answering application that extracts and chunks document text, converts the chunks into embeddings, indexes them with FAISS, retrieves relevant context for user questions, and uses OpenAI GPT to generate document-grounded answers.

## Author

**Rajesh Goud**

GitHub: [Rajesh3999](https://github.com/Rajesh3999)

---

### Disclaimer

This project is intended for educational and demonstration purposes.
