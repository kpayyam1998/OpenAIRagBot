from langchain_community.vectorstores import FAISS

from app.exceptions import RetrievalError

class VectorDB:
    def __init__(self, embeddings=None ):
        self.embeddings = embeddings
        self.vector_index = None

    def _createvectorDB(self , docs):
        """Creates a vector index from document embeddings."""
        try:
            self.vector_index = FAISS.from_documents(docs,self.embeddings)
            self.vector_index.save_local("creditcarddb")
        except Exception as e:
            raise RetrievalError(f"Failed to create vector index: {str(e)}")
        
    def _load_index(self):
        "Load Previously created index"

        try:
            self.vector_index = FAISS.load_local("creditcard_db",self.embeddings,allow_dangerous_deserialization=True)
        except Exception as e:
            raise RetrievalError(f"Failed to load vector index: {str(e)}")
        
    def _retrieve(self,query_embedding,top_n=5):
        """Retrieve top N documents from the vector database."""
        try:
            retriever = self.vector_index.as_retriever()
            return retriever.retrieve(query_embedding, top_k=top_n)
        except Exception as e:
            raise RetrievalError(f"Failed to retrieve documents: {str(e)}")
        




        
