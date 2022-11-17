from os import remove

import playsound
from gtts import gTTS


def en_speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('audio.mp3')
    print(f'Bot: {text}')
    playsound.playsound('audio.mp3')
    remove('audio.mp3')


def bn_speak(text):
    tts = gTTS(text=text, lang='bn')
    tts.save('bnaudio.mp3')
    print(f'Bot: {text}')
    playsound.playsound('bnaudio.mp3')
    remove('bnaudio.mp3')


def hi_speak(text):
    tts = gTTS(text=text, lang='hi')
    tts.save('hiaudio.mp3')
    print(f'Bot: {text}')
    playsound.playsound('hiaudio.mp3')
    remove('hiaudio.mp3')


def ar_speak(text):
    tts = gTTS(text=text, lang='ar')
    tts.save('araudio.mp3')
    print(f'Bot: {text}')
    playsound.playsound('araudio.mp3')
    remove('araudio.mp3')
