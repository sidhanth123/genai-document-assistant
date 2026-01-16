import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st

from backend.document_loader import load_documents
from backend.text_splitter import split_documents
from backend.embeddings import get_embeddings
from backend.vector_store import create_vector_store
from backend.rag_pipeline import create_rag_chain

st.set_page_config(
    page_title="AI Document Intelligence Assistant",
    layout="wide"
)

st.title("📄 AI-Powered Business Document Assistant")
st.write("Ask questions directly from uploaded documents using GenAI (RAG).")

@st.cache_resource
def initialize_rag():
    docs = load_documents("data/documents")
    chunks = split_documents(docs)
    embeddings = get_embeddings()
    vector_store = create_vector_store(chunks, embeddings)
    qa_chain = create_rag_chain(vector_store)
    return qa_chain

qa_chain = initialize_rag()

query = st.text_input("Enter your question:")

if query:
    with st.spinner("Generating answer..."):
        answer = qa_chain(query)
        st.subheader("Answer")
        st.write(answer)
