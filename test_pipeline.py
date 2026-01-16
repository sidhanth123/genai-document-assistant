from backend.document_loader import load_documents
from backend.text_splitter import split_documents
from backend.embeddings import get_embeddings
from backend.vector_store import create_vector_store
from backend.rag_pipeline import create_rag_chain

docs = load_documents("data/documents")
print("Documents loaded:", len(docs))

chunks = split_documents(docs)
print("Chunks created:", len(chunks))

embeddings = get_embeddings()
vector_store = create_vector_store(chunks, embeddings)

qa_chain = create_rag_chain(vector_store)

result = qa_chain.run("What is this document about?")
print("Answer:", result)
