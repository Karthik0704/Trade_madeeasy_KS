from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DELTA_API_KEY = os.getenv('DELTA_API_KEY')
ANOTHER_API_KEY = os.getenv('ANOTHER_API_KEY')
DELTA_BASE_URL = os.getenv('DELTA_BASE_URL')