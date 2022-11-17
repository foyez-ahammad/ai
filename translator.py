import os
from time import sleep

import playsound
import speech_recognition as sr
import translators as ts
from base import speak, take_command
from googletrans import Translator
from gtts import gTTS


def lang_listen(lang):
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            recognizer = listener.recognize_google(voice, language=lang)
            recognizer = recognizer.lower()
            print(f'you: {recognizer}')
    except:
        return 'None'
    return recognizer


def lang_speak(text, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save('audio.mp3')
    print(f'Bot: {text}')
    playsound.playsound('audio.mp3')
    os.remove('audio.mp3')


t = Translator()

def en_to_bn():
    english = lang_listen('en')
    lang_speak(t.translate(english, src='en', dest='bn').text, 'bn')

def bn_to_en():
    bangla = lang_listen('bn')
    lang_speak(t.translate(bangla, src='bn', dest='en').text, 'en')

def trans():
    speak('Sir! which languages between should i select?')
    while True:
        command = take_command()
        if 'sleep' in command:
            speak('Okay Sir')
            break

        # elif 'english between bangla' in command:
        else:
            speak('Okay Sir! First speak english speaker.')
            while True:
                # if 'jarvis stop' in command:
                #     speak('Okay Sir!')
                #     break
                # else:
                # en_to_bn()
                # sleep(1)
                # bn_to_en()
                # sleep(1)
                bangla = lang_listen('bn')
                lang_speak(t.translate(bangla, dest='en').text, 'en')
trans()