# from pydantic import BaseModel,HttpUrl,ValidationError  as PydanticValidationError
# from pydantic import ValidationError

# class DocumentIngestionRequest(BaseModel):
#     url: list[HttpUrl] # Expecting a list of urls

# class QueryRequest(BaseModel):
#     question : str # empty string

# def validationDocumentIngestion(data):
#     try:
#         DocumentIngestionRequest(data)
#         #return True
#     except PydanticValidationError as e:
#         raise ValidationError(f"Document ingestion validation error: {e}")
    
# def validationQueryRequest(data):
#     try:
#         QueryRequest(**data)
#         # return True
#     except PydanticValidationError as e:
#         raise ValidationError(f"Query validation error: {e}")
