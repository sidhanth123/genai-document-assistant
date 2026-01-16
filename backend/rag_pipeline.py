from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline

def create_rag_chain(vector_store):
    pipe = pipeline(
        "text-generation",
        model="google/flan-t5-base",
        max_new_tokens=256
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    def qa_run(query: str):
        docs = retriever.invoke(query)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
        Answer the question using ONLY the context below.
        If the answer is not present, say "I don't know."

        Context:
        {context}

        Question:
        {query}
        """

        # ✅ Correct invocation
        response = llm.invoke(prompt)

        # HuggingFacePipeline may return string or dict depending on version
        if isinstance(response, dict):
            return response.get("text", "")
        return response

    return qa_run
