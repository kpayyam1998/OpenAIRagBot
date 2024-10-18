import os

from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


from app.base import DocumentProcessor
from app.validators import validationDocumentIngestion


class DocumentIngestor(DocumentProcessor):

    def __init__(self, embedding_cretor):
        self.embedding_cretor = embedding_cretor

    def ingest_document(self, urls):

        validationDocumentIngestion(urls)

        loader = UnstructuredURLLoader(urls)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        return docs
