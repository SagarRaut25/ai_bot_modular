import logging
import cohere
from config import Config

logger = logging.getLogger(__name__)

# Initialize Cohere client
co = cohere.Client(Config.COHERE_API_KEY)


def generate_dynamic_follow_up(conversation_history, current_topic):
    logger.debug(f"Generating dynamic follow-up for topic: {current_topic}")
    try:
        prompt = f"""
        Based on the candidate's last response about '{current_topic}', generate a relevant, insightful follow-up question.
        The question should:
        1. Be directly related to specific details in their response
        2. Probe deeper into their experience, knowledge, or thought process
        3. Be professional and appropriate for a job interview
        4. Be concise (one sentence)
        
        Candidate's last response: "{conversation_history[-1]['text']}"
        
        Return ONLY the question, nothing else.
        """
        response = co.generate(
            model="command-r-plus",
            prompt=prompt,
            max_tokens=200,
            temperature=0.7
        )
        follow_up = response.generations[0].text.strip()
        logger.debug(f"Generated follow-up question: {follow_up}")
        return follow_up if follow_up.endswith('?') else follow_up + '?'
    except Exception as e:
        logger.error(f"Error generating dynamic follow-up: {str(e)}", exc_info=True)
        return None