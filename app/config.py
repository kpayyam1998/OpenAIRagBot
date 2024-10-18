import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        self.api_key =None
        load_dotenv()  # Load environment variables from.env file

    def get_api_key(self):
        self.api_key = os.getenv('OPENAI_API_KEY')

        if self.api_key is None:
            raise ValueError('OPENAI_API_KEY environment variable not found')
        
        return self.api_key