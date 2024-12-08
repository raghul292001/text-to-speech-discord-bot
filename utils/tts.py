
#ggts library

# from gtts import gTTS
# import os

# def text_to_speech(text: str, filename: str = "response.mp3", lang="en", tld="co.in") -> str:
#     """
#     Convert text to speech and save as an audio file.

#     :param text: The text to convert to speech.
#     :param filename: Filename for the generated audio file.
#     :param lang: Language for TTS (default: English).
#     :param tld: Top-level domain (used to modify accent, default is "com" for standard US English).
#     :return: The path to the saved audio file.
#     """
#     try:
#         # Use the gTTS library to convert the text to speech with the specified parameters
#         tts = gTTS(text=text, lang=lang, tld=tld,slow=False)
#         tts.save(filename)
#         return filename
#     except Exception as e:
#         raise RuntimeError(f"Error converting text to speech: {str(e)}")

#pyttsx3 library

import pyttsx3
import os

# def text_to_speech(text: str, filename: str = "response.mp3") -> str:
#     """
#     Convert text to speech using pyttsx3 and save as an audio file.
    
#     :param text: The text to convert to speech.
#     :param filename: Filename for the generated audio file.
#     :return: The path to the saved audio file.
#     """
    # try:
    #     # Initialize the pyttsx3 engine
    #     engine = pyttsx3.init()

    #     # Set properties for voice (male voice)
    #     voices = engine.getProperty('voices')
        
    #     # Select the first male voice
    #     male_voice = None
    #     for voice in voices:
    #         if "male" in voice.id.lower():
    #             male_voice = voice
    #             break

    #     if male_voice:
    #         engine.setProperty('voice', male_voice.id)
    #     else:
    #         # Fallback if no male voice is found
    #         engine.setProperty('voice', voices[0].id)  # Default male voice on most systems

    #     # Set speaking rate (optional)
    #     engine.setProperty('rate', 150)  # Adjust rate if needed

    #     # Save the speech to an audio file
    #     engine.save_to_file(text, filename)
    #     engine.runAndWait()

    #     return filename
    # except Exception as e:
    #     raise RuntimeError(f"Error converting text to speech: {str(e)}")

def set_natural_voice():
    """
    Sets the TTS engine to a natural-sounding male voice.
    """
    engine = pyttsx3.init()

    # Get all available voices
    voices = engine.getProperty('voices')

    # Set a natural male voice (for example, 'Microsoft Mark')
    for voice in voices:
        if 'George' in voice.name:  # Microsoft Mark is a natural-sounding male voice
            engine.setProperty('voice', voice.id)
            print(f"Selected Voice: {voice.name}")
            break
    return engine

def text_to_speech(text: str, filename: str = "response.wav") -> str:
    """
    Convert text to speech and save as an audio file.

    :param text: The text to convert to speech.
    :param filename: Filename for the generated audio file.
    :return: The path to the saved audio file.
    """
    try:
        engine = set_natural_voice()  # Set the natural voice

        # Set properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

        # Save the generated speech to a file
        engine.save_to_file(text, filename)
        engine.runAndWait()

        return filename
    except Exception as e:
        raise RuntimeError(f"Error converting text to speech: {str(e)}")
