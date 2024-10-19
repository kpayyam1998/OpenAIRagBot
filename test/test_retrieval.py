import time
from app.main import RAGBot  # Assuming RAGBot is defined in app.rag_bot
from app.exceptions import ValidationError

def test_document_retrieval():
    rag_bot = RAGBot()

    # Test Case: List of URLs to ingest
    document_urls = [
        "https://www.icicibank.com/personal-banking/cards/credit-card",
        "https://www.hdfcbank.com/personal/pay/cards/credit-cards",
        # Add more URLs as needed
    ]

    try:
        # Ingest documents and create the vector database
        start_time = time.time()
        rag_bot._ingest_document(document_urls)
        end_time = time.time()
        print(f"Document Ingestion Time: {end_time - start_time:.2f} seconds")
        
        # Test retrieval with a query
        question = "What are the benefits of a credit card?"
        retrieval_start_time = time.time()
        retriever = rag_bot.vector_db._retrieve()
        result, sources = rag_bot.vector_db._final_results(retriever, question)
        retrieval_end_time = time.time()

        print(f"Retrieved Answer: {result}")
        print(f"Retrieved Sources: {sources}")
        print(f"Retrieval Time: {retrieval_end_time - retrieval_start_time:.2f} seconds")

    except ValidationError as e:
        print(f"Validation error during document ingestion/retrieval: {e}")
    except Exception as e:
        print(f"Unexpected error during document retrieval: {e}")

if __name__ == "__main__":
    # Run the test
    test_document_retrieval()
