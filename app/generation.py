# app/generation.py
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_openai import OpenAI
from app.exceptions import RAGBotException

class ResponseGenerator:
    def __init__(self):
        self.llm = OpenAI(temperature=0.9, max_tokens=400)

    def generate_response(self, query, retriever):
        """Generate a response using the LLM based on the query and retrieved documents."""
        try:
            chain = RetrievalQAWithSourcesChain.from_chain_type(self.llm, chain_type="stuff", retriever=retriever)
            response = chain({"question": query}, return_only_outputs=True)
            return response
        except Exception as e:
            raise RAGBotException(f"Error generating response: {e}")
