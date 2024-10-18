from app.config import Config
from app.ingestion import DocumentIngestor
from app.embeddings import OpenAIEmbeddingProcessor
from app.retrieval import VectorDB
from app.generation import ResponseGenerator
from app.validators import validationQueryRequest
from exceptions import ValidationError


class RAGBot:
    def __init__(self):
        self.embedding_creator = OpenAIEmbeddingProcessor()
        self.docuement_ingestor = DocumentIngestor(self.embedding_creator)
        self.vector_db = VectorDB(self.embedding_creator)
        self.response_generator = ResponseGenerator()

    def _ingestDocument(self, urls:list):

        "Process URL"
        if not urls:
            raise ValidationError("No URLs provided")
        
        docs = self.docuement_ingestor.ingest_document(urls)

        embeddings = self.embedding_creator.embed_document(docs)

        # Create VectorDB
        self.vector_db._createvectorDB(docs)
        print("VectorDB created")
    
    def generate_response(self, question: str):
        """Run the RAG bot process to generate a response to a query."""
        if not question:
            raise ValidationError("Question is required")

        # Validate the query
        validationQueryRequest({"question": question})

        # Embed the query
        query_embedding = self.embedding_creator.embed_query(question)

        # Retrieve relevant documents from vector DB
        self.vector_db._load_index()
        relevant_docs = self.vector_db.retrieve(query_embedding)

        # Generate the response using the retrieved documents
        response = self.response_generator.generate_response(question, self.vector_db.vector_index)
        return response


if __name__ == "__main__":
    # Instantiate the RAGBot object
    rag_bot = RAGBot()

    # Sample test: Ingest documents
    try:
        # Provide a list of URLs for testing ingestion
        document_urls = [
            "https://www.icicibank.com/personal-banking/cards/credit-card",
            "https://www.hdfcbank.com/personal/pay/cards/credit-cards",
        ]
        rag_bot._ingestDocument(document_urls)
    except ValidationError as e:
        print(f"Ingestion failed: {e}")
    except Exception as e:
        print(f"Unexpected error during ingestion: {e}")

    # Sample test: Generate response
    try:
        question = "Benifits of Freedom Credit Card?."
        response = rag_bot.generate_response(question)
        print("Generated Response:", response)
    except ValidationError as e:
        print(f"Failed to generate response: {e}")
    except Exception as e:
        print(f"Unexpected error during response generation: {e}")