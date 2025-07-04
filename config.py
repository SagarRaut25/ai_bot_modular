import os
from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()
# print("COHERE_API_KEY from .env:", os.getenv('COHERE_API_KEY'))



import os
from dotenv import load_dotenv

load_dotenv()



class Config:
    # Flask Session Configurations
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    SESSION_TYPE = 'filesystem'
    SESSION_COOKIE_NAME = 'session'
    SESSION_FILE_DIR = os.path.join(os.getcwd(), 'flask_session_data')

    SESSION_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SECURE = True

    # Cohere API Key - Loaded securely from environment variables
    COHERE_API_KEY = os.getenv('COHERE_API_KEY', 'your-cohere-api-key-here')  # Default for dev

    # Django API URL
    DJANGO_API_URL = os.getenv('DJANGO_API_URL')


    # Interview Configuration
    MAX_RECORDING_DURATION = 520  # Max duration for recording (in seconds)
    PAUSE_THRESHOLD = 40  # Threshold in seconds for pause detection
    FOLLOW_UP_PROBABILITY = 0.8  # Probability of asking follow-up questions
    MAX_FOLLOW_UPS = 3  # Maximum number of follow-ups per question
    MIN_FOLLOW_UPS = 2  # Minimum number of follow-ups per question

    # File Configuration
    CONVERSATION_FILE = "interview_conversation.txt"
    LOG_FILE = 'interview_app.log'
