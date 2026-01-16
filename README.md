# AI-Powered Document Intelligence Assistant (GenAI RAG)

An end-to-end **Retrieval-Augmented Generation (RAG)** application that enables users to ask natural-language questions and receive accurate, context-grounded answers from complex insurance and policy documents.

This project demonstrates how GenAI can be applied to real-world enterprise documents such as insurance policies, compliance manuals, and corporate guidelines.

---

# Key Features

- PDF document ingestion and preprocessing  
- Semantic search using vector embeddings  
- Retrieval-Augmented Generation (RAG) for accurate answers  
- Fully local embeddings and LLM (no paid API dependency)  
- Interactive Streamlit web interface  
- Designed to minimize hallucinations by restricting answers to document context  

---

# Problem Statement

Enterprise documents such as insurance policies and legal agreements are lengthy, complex, and difficult to query manually.  
This project solves that problem by allowing users to **ask questions in plain English** and receive precise answers grounded strictly in the document content.

---

# System Architecture

1. PDF documents are loaded and split into smaller text chunks  
2. Chunks are converted into vector embeddings  
3. FAISS is used for fast similarity-based retrieval  
4. A local instruction-tuned language model generates answers using retrieved context  
5. Streamlit provides an interactive user interface  

---

# 🛠️ Tech Stack

- **Programming Language:** Python  
- **Frameworks & Libraries:**  
  - LangChain  
  - FAISS  
  - SentenceTransformers  
  - Hugging Face Transformers  
  - Streamlit  
- **LLM:** Local instruction-tuned model (FLAN-T5)  
- **Embedding Model:** all-MiniLM-L6-v2  

---

# Project Structure

genai-document-assistant/
│
├── app/
│ └── app.py
│
├── backend/
│ ├── document_loader.py
│ ├── text_splitter.py
│ ├── embeddings.py
│ ├── vector_store.py
│ └── rag_pipeline.py
│
├── data/
│ └── documents/
│ └── insurance_policy.pdf
│
├── requirements.txt
├── test_pipeline.py
├── README.md
└── .gitignore

# How to Run the Project

# 1. Clone the Repository
```bash
git clone https://github.com/your-username/genai-document-assistant.git
cd genai-document-assistant

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Add PDF Document

Place your insurance or policy PDF inside:

data/documents/

5. Run the Application
streamlit run app/app.py

🧪 Sample Questions You Can Ask

What type of insurance policy is this?

What are the main exclusions under this policy?

How does the policy define a “Claim”?

Does this policy cover fraud or employee dishonesty?

What is the limit of liability under this policy?

# Use Cases

Insurance policy analysis

Legal and compliance document Q&A

Corporate policy search

Internal knowledge assistants

# Resume Highlight

Built a GenAI-powered document intelligence assistant using Retrieval-Augmented Generation (RAG) with local embeddings and LLMs, enabling accurate question answering on complex insurance policy documents.

# License

This project is for educational and demonstration purposes.




