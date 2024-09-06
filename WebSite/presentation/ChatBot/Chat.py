import speech_recognition as sr
import os
from gtts import gTTS
import requests

# Initialize the speech recognition library
r = sr.Recognizer()

# Initialize the Gemini API endpoint
gemini_api_endpoint = "https://gemini.google.com/app"

while True:
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Convert the audio to text
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)

        # Send the text to the Gemini API to get the answer
        response = requests.post(gemini_api_endpoint, json={"query": text})
        answer = response.json()["answer"]

        # Convert the answer to audio and read it aloud
        tts = gTTS(text=answer, lang='en')
        tts.save("answer.mp3")
        os.system("mpg321 answer.mp3")

    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
    except sr.RequestError as e:
        print("Error; {0}".format(e))