import speech_recognition as sr
import tempfile
import os


def transcribe_audio(audio_file):

    recognizer = sr.Recognizer()

    # Create temporary audio file
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    ) as temp:

        temp.write(audio_file.read())
        temp_path = temp.name

    try:

        with sr.AudioFile(temp_path) as source:

            audio = recognizer.record(source)

        try:

            text = recognizer.recognize_google(
                audio
            )

            return text

        except sr.UnknownValueError:

            return (
                "Sorry, the speech could not be understood."
            )

        except sr.RequestError as e:

            return (
                f"Speech recognition service error: {e}"
            )

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)