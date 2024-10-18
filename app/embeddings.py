from langchain_openai.embeddings import OpenAIEmbeddings
from app.base import EmbeddingProcessor


class OpenAIEmbeddingProcessor(EmbeddingProcessor):
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()


    def embed_document(self, docs):
        return self.embeddings.embed_documents(docs)
    
    def embed_query(self, queries):
        return self.embeddings.embed_query(queries)