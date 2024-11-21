from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY=os.getenv('GEMINI_API_KEY')
SERVER_URL='localhost'
PORT ='8900'
ENV='dev'