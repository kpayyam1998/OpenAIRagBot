import os
from pathlib import Path


list_of_files =[
    "research/research.ipynb",
    "app/__init__.py",
    "app/main.py",
    "app/ingestion.py",
    "app/retrieval.py",
    "app/generation.py",
    "app/embeddings.py",
    "app/config.py",
    "models/__init__.py",
    "models/retriever/__init__.py",
    "models/generator/__init__.py",
    "data/__init__.py",
    "utils/__init__.py",
    "utils/helper.py",
    "vectordb/__init__.py",
    "test/__init__.py",
    "test/test_retrieval.py",
    "test/test_generation.py",
    "test/test_endpoints.py",
    "requirements.txt",
    ".env",
    ".gitignore",
    "README.md",
    "app.py"

]

for files in list_of_files:

    file_path=Path(files)

    # Split files dir and file name
    file_dir,file_name=os.path.split(files)

    if file_dir:
        # Create directory if not exists
        os.makedirs(file_dir, exist_ok=True)
        print(f"Created directory: {file_dir}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open( file_path , "w" ) as f:
            pass
            print(f"Created file: {file_path}")
    else:
        print(f"Path is already created: {file_path}")
        

