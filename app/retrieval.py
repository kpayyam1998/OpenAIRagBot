from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain

from app.exceptions import RetrievalError

class VectorDB:
    def __init__(self ):
        self.embeddings = OpenAIEmbeddings()
        self.vector_index = None
        self.openai=OpenAI(temperature=0.9,max_tokens=400)

    def _createvectorDB(self , docs):
        """Creates a vector index from document embeddings."""
        try:
            self.vector_index = FAISS.from_documents(docs,self.embeddings)
            self.vector_index.save_local("creditcard_db")
        except Exception as e:
            raise RetrievalError(f"Failed to create vector index: {str(e)}")
        
    def _load_index(self):
        "Load Previously created index"

        try:
            self.vector_index = FAISS.load_local("creditcard_db",self.embeddings,allow_dangerous_deserialization=True)

        except Exception as e:
            raise RetrievalError(f"Failed to load vector index: {str(e)}")
        
    def _retrieve(self):
        """Retrieve top N documents from the vector database."""
        try:
            self._load_index()
            retriever = self.vector_index.as_retriever(search_kwargs={'k': 3, 'lambda_mult': 0.25})
            return retriever
        except Exception as e:
            raise RetrievalError(f"Failed to retrieve documents: {str(e)}")
        
    def _finalResults(self,retriever,question):
        try:
            chain=RetrievalQAWithSourcesChain.from_chain_type(self.openai, chain_type="stuff", retriever=retriever)
            response=chain({
                "question": question
            },return_only_outputs=True)

            return (response['answer'],response['sources'])
        except Exception as e:
            raise RetrievalError(f"Failed to create retrieval chain: {str(e)}")

        
        




        
