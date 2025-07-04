# # services/tts_service.py

# import base64
# import tempfile
# import os
# import logging
# from gtts import gTTS
# from gtts.tts import gTTSError


# logger = logging.getLogger(__name__)

# def text_to_speech(text: str) -> str:
#     """
#     Converts input text to speech using Google Text-to-Speech (gTTS)
#     and returns the MP3 audio as a base64-encoded string.
#     """
#     logger.debug(f"Converting text to speech: {text[:50]}...")  # Log preview of text
#     try:
#         # Generate audio using gTTS
#         tts = gTTS(text=text, lang='en', slow=False)

#         # Write to temporary file
#         with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
#             temp_filename = temp_file.name
#             tts.save(temp_filename)

#         # Read and encode the MP3 file
#         with open(temp_filename, 'rb') as f:
#             audio_data = f.read()

#         # Cleanup
#         os.unlink(temp_filename)

#         # Return base64-encoded audio
#         logger.debug("Successfully converted text to base64 audio")
#         return base64.b64encode(audio_data).decode('utf-8')

#     except Exception as e:
#         logger.error(f"Text-to-speech error: {str(e)}", exc_info=True)
#         return None




# import base64
# import tempfile
# import os
# import logging
# from gtts import gTTS
# from gtts.tts import gTTSError  # ✅ NEW import

# logger = logging.getLogger(__name__)

# def text_to_speech(text: str) -> str:
#     """
#     Converts input text to speech using gTTS (Google Text-to-Speech)
#     and returns the audio as a base64-encoded MP3 string.
#     Returns None on failure.
#     """
#     logger.debug(f"Converting text to speech: {text[:50]}...")

#     try:
#         # Generate TTS and save to file
#         tts = gTTS(text=text, lang='en', slow=False)
#         with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
#             temp_filename = temp_file.name
#             tts.save(temp_filename)

#         # Read and encode
#         with open(temp_filename, 'rb') as f:
#             audio_data = f.read()

#         # Clean up file
#         os.unlink(temp_filename)

#         logger.debug("Successfully converted to base64 audio")
#         return base64.b64encode(audio_data).decode('utf-8')

#     except gTTSError as e:
#         logger.error(f"gTTS 429 or connection error: {str(e)}")
#         # ❌ Too Many Requests or Network issue — return None (React will handle gracefully)
#         return None

#     except Exception as e:
#         logger.error(f"General text-to-speech error: {str(e)}", exc_info=True)
#         return None







import base64
import tempfile
import os
import logging
from gtts import gTTS
from gtts.tts import gTTSError

logger = logging.getLogger(__name__)

def text_to_speech(text: str) -> str:
    """
    Converts input text to speech using gTTS and returns
    a data URI (base64-encoded MP3 audio).
    """
    logger.debug(f"Converting text to speech: {text[:50]}...")

    try:
        tts = gTTS(text=text, lang='en', slow=False)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
            temp_filename = temp_file.name
            tts.save(temp_filename)

        with open(temp_filename, 'rb') as f:
            audio_data = f.read()

        os.unlink(temp_filename)

        logger.debug("Successfully converted to base64 audio")
        # return f"data:audio/mpeg;base64,{base64.b64encode(audio_data).decode('utf-8')}"
        return base64.b64encode(audio_data).decode("utf-8")

    except gTTSError as e:
        logger.error(f"gTTS 429 or connection error: {str(e)}")
        return None

    except Exception as e:
        logger.error(f"General text-to-speech error: {str(e)}", exc_info=True)
        return None