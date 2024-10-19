from app.ingestion import DocumentIngestor
from app.embeddings import OpenAIEmbeddingProcessor
from app.validators import validationQueryRequest
from app.exceptions import ValidationError

from app.retrieval import VectorDB
class RAGBot:
    def __init__(self):
        self.embedding_creator = OpenAIEmbeddingProcessor()
        self.document_ingestor = DocumentIngestor(self.embedding_creator)
        self.vector_db = VectorDB()
        self.result = None
        self.source = None

    def _ingest_document(self, urls: list):
        """Process URLs."""
        if not urls:
            raise ValidationError("No URLs provided")
        
        # Ingest documents
        docs = self.document_ingestor.ingest_document(urls)

        # Create VectorDB
        self.vector_db._create_vector_db(docs)

    def generate_response(self, question: str):
        """Run the RAG bot process to generate a response to a query."""
        if not question:
            raise ValidationError("Question is required")

        # Retrieve relevant documents from vector DB
        retriever = self.vector_db._retrieve()

        # Generate the response using the retrieved documents
        self.result, self.source = self.vector_db._final_results(retriever, question)
        return self.result


if __name__ == "__main__":
    # Instantiate the RAGBot object
    rag_bot = RAGBot()

    # Sample test: Ingest documents
    try:
        document_urls = [
            "https://www.icicibank.com/personal-banking/cards/credit-card",
            "https://www.hdfcbank.com/personal/pay/cards/credit-cards",
        ]
        rag_bot._ingest_document(document_urls)
    except ValidationError as e:
        print(f"Ingestion failed: {e}")
    except Exception as e:
        print(f"Unexpected error during ingestion: {e}")

    # Sample test: Generate response
    try:
        question = "Benefits of Freedom Credit Card?"
        response = rag_bot.generate_response(question)
        print("Generated Response:", response)
    except ValidationError as e:
        print(f"Failed to generate response: {e}")
    except Exception as e:
        print(f"Unexpected error during response generation: {e}")