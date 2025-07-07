import logging
import cohere
from config import Config

logger = logging.getLogger(__name__)

# Initialize Cohere client with API key from config
co = cohere.Client(Config.COHERE_API_KEY)


import logging
import cohere
from config import Config

logger = logging.getLogger(__name__)

# Initialize Cohere client
co = cohere.Client(Config.COHERE_API_KEY)


def generate_encouragement_prompt(conversation_history):
    """
    Generate a brief encouragement prompt if the user has paused too long during the interview.
    """
    logger.debug("Generating encouragement prompt for paused candidate")

    try:
        prompt = f"""
        The candidate has paused during their response. Generate a brief, encouraging prompt to:
        - Help them continue their thought
        - Reference specific aspects of their previous answers
        - Be supportive and professional
        - Be concise (one short sentence)
        
        Current conversation context:
        {conversation_history[-2:]}
        
        Return ONLY the prompt, nothing else.
        """

        response = co.generate(
            model="command-r-plus",
            prompt=prompt,
            max_tokens=300,
            temperature=0.5
        )

        encouragement = response.generations[0].text.strip()
        logger.debug(f"Generated encouragement: {encouragement}")
        return encouragement

    except Exception as e:
        logger.error(f"Error generating encouragement prompt: {str(e)}", exc_info=True)
        return "Please continue with your thought."

