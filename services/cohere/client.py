import cohere
from config import Config

# Initialize and expose Cohere client
co = cohere.Client(Config.COHERE_API_KEY)
