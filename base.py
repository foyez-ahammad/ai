# Installed Module
import pyttsx3
import speech_recognition as sr

# For "voice recognize", "text to speech" and "voice property"
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)  # have 4 voices
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    print(f'Bot: {audio}')
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            recognizer = listener.recognize_google(voice)
            recognizer = recognizer.lower()
            print(f'You: {recognizer}')
    except:
        return 'None'
    return recognizer
