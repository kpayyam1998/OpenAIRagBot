import time
from app.main import RAGBot  # Assuming RAGBot is defined in app.rag_bot
from app.exceptions import ValidationError

def test_response_generation():
    rag_bot = RAGBot()

    # Test Cases
    questions = [
        "What are the benefits of a credit card?",
        "How do I apply for a loan?",
        "What is the interest rate for savings accounts?",
        # Add more questions as needed
    ]

    try:
        # Benchmarking each question
        for question in questions:
            start_time = time.time()
            response = rag_bot.generate_response(question)
            end_time = time.time()

            print(f"Question: {question}")
            print(f"Generated Response: {response}")
            print(f"Time Taken: {end_time - start_time:.2f} seconds")
            print("-" * 40)
    except ValidationError as e:
        print(f"Validation error during response generation: {e}")
    except Exception as e:
        print(f"Unexpected error during response generation: {e}")

if __name__ == "__main__":
    # Run the test
    test_response_generation()
