Absolutely. Since this is a **RAG Book Assistant** built with Streamlit, Chroma, Hugging Face embeddings, and Mistral, you can use the following as your `README.md`.

# 📚 RAG Book Assistant

A **Retrieval-Augmented Generation (RAG)** application that allows users to upload a PDF book and ask questions about its content.

The application processes the uploaded PDF, splits it into smaller chunks, converts those chunks into vector embeddings using **Hugging Face Sentence Transformers**, stores them in **ChromaDB**, retrieves the most relevant content for a user's question, and uses **Mistral AI** to generate an answer based only on the retrieved context.

---

## 🚀 Features

* 📄 Upload PDF books
* ✂️ Split documents into smaller chunks
* 🤗 Generate embeddings using Hugging Face
* 🗄️ Store embeddings in ChromaDB
* 🔎 Semantic search using vector similarity
* 🎯 MMR-based retrieval for diverse and relevant results
* 🤖 Generate answers using Mistral AI
* 🔐 Answers are restricted to the uploaded document
* 🌐 Simple and interactive Streamlit UI

---

## 🏗️ Application Architecture

```text
                    ┌─────────────────┐
                    │    PDF Book     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  PyPDFLoader    │
                    │ Load PDF Pages  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Text Splitter   │
                    │ Chunk Size 1000 │
                    │ Overlap 200     │
                    └────────┬────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │ Hugging Face Embeddings  │
                │ all-MiniLM-L6-v2         │
                └────────────┬─────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    ChromaDB     │
                    │ Vector Database │
                    └────────┬────────┘
                             │
                     User Question
                             │
                             ▼
                    ┌─────────────────┐
                    │ MMR Retriever   │
                    │ Top K = 4       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Retrieved       │
                    │ Context         │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Mistral AI    │
                    │      LLM        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   AI Answer     │
                    └─────────────────┘
```

---

## 🔄 How It Works

The application follows a typical **Retrieval-Augmented Generation (RAG)** pipeline.

### 1. Upload PDF

The user uploads a PDF book through the Streamlit interface.

The PDF is temporarily stored on the local system.

### 2. Load the PDF

`PyPDFLoader` reads the PDF and extracts the text from each page.

```python
loader = PyPDFLoader(file_path)
docs = loader.load()
```

### 3. Split the Document

Large documents are divided into smaller chunks using `RecursiveCharacterTextSplitter`.

```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)
```

Chunking makes it easier to retrieve only the relevant portions of the document.

### 4. Generate Embeddings

Each text chunk is converted into a numerical vector using the Hugging Face model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

The embedding represents the semantic meaning of the text.

```python
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```

### 5. Store Vectors in ChromaDB

The generated embeddings are stored in ChromaDB.

```python
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)
```

This allows the application to perform semantic searches later.

### 6. User Asks a Question

The user enters a question such as:

```text
What is the main idea discussed in Chapter 3?
```

The question is converted into an embedding and compared with the document embeddings.

### 7. Retrieve Relevant Content

The application uses an MMR retriever:

```python
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)
```

MMR (Maximal Marginal Relevance) attempts to return results that are both relevant to the question and sufficiently diverse.

### 8. Generate the Answer

The retrieved chunks are passed to Mistral AI along with the user's question.

The system prompt instructs the model to answer **only using the retrieved document context**.

If the required information isn't available, the model is instructed to respond:

```text
I could not find the answer in the document.
```

---

## 🛠️ Tech Stack

| Technology                     | Purpose                         |
| ------------------------------ | ------------------------------- |
| Python                         | Application development         |
| Streamlit                      | Web interface                   |
| LangChain                      | RAG orchestration               |
| PyPDFLoader                    | PDF text extraction             |
| RecursiveCharacterTextSplitter | Document chunking               |
| Hugging Face                   | Text embeddings                 |
| Sentence Transformers          | Embedding model                 |
| ChromaDB                       | Vector database                 |
| Mistral AI                     | Large Language Model            |
| python-dotenv                  | Environment variable management |

---

## 📁 Project Structure

```text
RAG/
│
├── app.py
├── create_database.py
├── main.py
├── pdf.py
├── requirements.txt
│
└── chroma_db/
    └── Vector database files
```

### File Description

#### `app.py`

Main Streamlit application.

Responsible for:

* PDF upload
* Vector database creation
* Question input
* Document retrieval
* Answer generation

#### `create_database.py`

Contains functionality related to creating the vector database from document data.

#### `pdf.py`

Contains PDF-related processing functionality.

#### `main.py`

Application/helper entry point depending on the project structure.

#### `requirements.txt`

Contains the Python dependencies required to run the application.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Genrative-AI.git
```

Navigate into the project:

```bash
cd Genrative-AI/RAG
```

---

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If Hugging Face embeddings are being installed separately:

```bash
pip install langchain-huggingface sentence-transformers torch torchvision
```

---

## 🔑 Environment Variables

The application uses Mistral AI for generating responses.

Create a `.env` file:

```text
MISTRAL_API_KEY=your_mistral_api_key
```

If your application uses the OpenAI API elsewhere, configure the required OpenAI key as well.

**Do not commit `.env` to GitHub.**

Add it to `.gitignore`:

```text
.env
.venv/
__pycache__/
chroma_db/
*.pyc
```

---

## ▶️ Running the Application

From the `RAG` directory:

```bash
streamlit run app.py
```

Streamlit will start the application and provide a local URL.

Open the URL in your browser.

---

## 🧪 Example Usage

### Step 1

Upload a PDF book.

Example:

```text
Machine Learning.pdf
```

### Step 2

Click:

```text
Create Vector Database
```

The application will:

```text
PDF
 ↓
Extract Text
 ↓
Create Chunks
 ↓
Generate Embeddings
 ↓
Store in ChromaDB
```

### Step 3

Ask a question:

```text
What is machine learning?
```

### Step 4

The application retrieves relevant sections from the PDF and sends them to Mistral AI.

Example:

```text
AI Answer:

Machine learning is a branch of artificial intelligence that
allows systems to learn patterns from data and make predictions
without being explicitly programmed for every task.
```

---

## 🧠 RAG vs Traditional LLM

A traditional LLM answers questions based primarily on the information learned during training.

This application uses RAG:

```text
User Question
      ↓
Search Document
      ↓
Retrieve Relevant Chunks
      ↓
Send Context + Question to LLM
      ↓
Generate Answer
```

This helps the application answer questions about **documents that were not part of the model's original training data**.

---

## 🔍 Why Use Hugging Face Embeddings?

Instead of relying on OpenAI embeddings, this project uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Advantages:

* Runs locally
* No separate embedding API cost
* No embedding API key required
* Fast for small and medium-sized documents
* Easy to integrate with LangChain

The Mistral model is still used for the final answer generation.

---

## 🎯 Retrieval Configuration

The project uses:

```python
search_type="mmr"
```

with:

```python
k=4
fetch_k=10
lambda_mult=0.5
```

### `k`

Number of documents returned to the LLM.

```text
k = 4
```

### `fetch_k`

Number of candidate documents initially considered by MMR.

```text
fetch_k = 10
```

### `lambda_mult`

Controls the balance between relevance and diversity.

```text
lambda_mult = 0.5
```

A value closer to `1` favors relevance, while a lower value gives more importance to diversity.

---

## 🔐 Hallucination Control

The system prompt explicitly tells the LLM:

```text
Use ONLY the provided context to answer the question.
```

If the information isn't available in the retrieved context, the model is instructed to say:

```text
I could not find the answer in the document.
```

This provides a basic mechanism for reducing hallucinations.

---

## ⚠️ Current Limitations

* Currently designed primarily for PDF documents.
* The vector database is stored locally.
* Large books may require more processing time.
* Retrieval quality depends on chunk size and embedding quality.
* The application currently uses a single persistent ChromaDB directory.
* Scanned/image-only PDFs may require OCR before text can be retrieved.

---

## 🚀 Future Improvements

Possible improvements include:

* 📚 Support multiple PDF books
* 🗂️ Separate vector databases for different documents
* 💬 Chat history and conversational memory
* 📌 Show source pages for every answer
* 🔎 Hybrid search using keyword + vector search
* 🧠 Reranking retrieved documents
* 📊 Retrieval evaluation
* 🖼️ OCR support for scanned PDFs
* ☁️ Deploy ChromaDB/vector storage to the cloud
* 🔐 User authentication
* 📈 RAG performance monitoring
* ⚡ Streaming LLM responses

---

## 📌 Key Concepts Demonstrated

This project demonstrates practical implementation of:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* Vector Databases
* Document Chunking
* MMR Retrieval
* Prompt Engineering
* Large Language Models
* Hugging Face Sentence Transformers
* LangChain
* Streamlit
* ChromaDB

---

## 👨‍💻 Author

**Lucky Chaturvedi**

Software Development Engineer | Python | Backend | Cloud | GenAI | Cybersecurity

---

## 📄 License

This project is intended for educational and demonstration purposes.
