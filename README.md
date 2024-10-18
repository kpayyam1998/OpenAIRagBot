rag-bot-backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py                # Main entry point for the API
│   ├── retrieval.py           # Document retrieval using BM25
│   ├── generation.py          # Text generation using OpenAI API
│   ├── preprocessing.py       # Preprocess user queries
│   └── config.py              # Configuration for OpenAI API key and other settings
│
├── models/
│   ├── retriever/             # BM25 retriever class and methods
│   └── generator/             # OpenAI generation class and methods
│
├── data/
│   ├── knowledge_base.json    # Documents or FAQs for the knowledge base
│
├── utils/
│   ├── logging_utils.py       # Helper functions for logging
│   └── security_utils.py      # Security functions (optional, not included here)
│
├── tests/
│   ├── test_retrieval.py      # Unit tests for retrieval
│   ├── test_generation.py     # Unit tests for generation
│   └── test_endpoints.py      # Unit tests for the main API
│
├── requirements.txt           # Dependencies
├── Dockerfile                 # For containerization (optional)
├── .env                       # API keys and environment variables
└── app.py                     # Main entry point to run the server


Project structure