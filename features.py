import datetime  # for @wish_me
import os  # for @random__song and @news and @translator
import random  # for @random__song
import webbrowser  # for @search
from time import sleep  # for @app_open

import keyboard  # for @app_open
import playsound  # for @news and @translator
import pyjokes  # for @joke
import pywhatkit as pykit  # for @play
import requests  # for @news
import speech_recognition as sr
import wikipedia  # for @search and 'wikipedia'
from base import speak, take_command  # import from base.py file
from bs4 import BeautifulSoup  # for @news
from googletrans import Translator  # for @translator
from gtts import gTTS  # for @news and @


def hold(data):
    digit = ''
    for sec in data:
        if sec.isdigit():
            digit += sec
    try:
        if digit != '':
            speak(f'Okay Sir! i am taking break for {digit} second')
            print('hold.....')
            result = int(digit)
            sleep(result)
            speak('Sir! Break time is over')
    except ValueError:
        speak('Sorry Sir! I did not understand. how many second?')
        sleep(3)


def talk():
    speak("Sir! which topic choosing for talking?")
    while True:
        command = take_command().lower()

        if ('ok' in command) or ('thank' in command):
            speak('Okay Sir!')
            break
        elif 'morning' in command:
            speak('Good Morning Sir! How are you?')
        elif 'evening' in command:
            speak('Good Evening Sir! How is going today!')
        elif 'night' in command:
            speak('Good Night Sir! Have a good day!')
        elif 'afternoon' in command:
            speak('Good Afternoon Sir! How are you?')
        elif 'how are you' in command:
            speak('Sir! I am fine. What about you?')
        elif 'fine' in command:
            speak('Sir! I wish you always be fine and happy.')
        elif 'pretty' in command:
            speak('So Sad Sir! I think, if you want i can switch your mode.')
        elif 'how' in command:
            speak('Sir! I have many option. Like, Listen to Music, Quran Reaction, Natural Sound and Mode Off lyrics')
        elif 'no need' in command:
            speak('Okay Sir! What Can I do for you?')
        elif 'ok' in command:
            speak('Sir! Which One am I play.')
        elif 'play quran' in command:
            speak('Okay Sir! Playing...')
            reactions = ['https://youtu.be/5R06LRdUCSE',
                         'https://youtu.be/jl6D6WDKZbc', ]
            random_reaction = random.choice(reactions)
            webbrowser.open(random_reaction)
        elif 'play song' in command:
            speak('Okay Sir! Playing...')
            songs = [
                'https://youtu.be/8IXUIhzz4I4', 'https://youtu.be/y4qtP1o8kCg',
                'https://youtu.be/KfXIF2Mm2Kc', 'https://youtu.be/u_-McEvEGvI',
                'https://youtu.be/caeTvZrlVTo', 'https://youtu.be/ViWAM7MfAg8',
                'https://youtu.be/cq_It-126nU',
            ]
            random_song = random.choice(islamic_songs)
            webbrowser.open(random_song)

        # About AI
        elif 'your name' in command:
            speak('Sir! My Name is Trisha')
        elif 'nice name' in command:
            speak('Thank You, Sir!')
        elif 'your age' in command:
            speak('My age is only 2 days')
        elif 'your birthday' in command:
            speak('My Birthday is 1 March 2022')
        elif 'your owner' in command:
            speak('Foyez Ahammad Machum Sir!')
        elif 'your creator' in command:
            speak('Foyez Ahammad Machum Sir!')
        elif 'your boss' in command:
            speak('Foyez Ahammad Machum Sir!')
        elif 'your friend' in command:
            speak('Foyez Ahammad Machum Sir!')
        elif 'marry me' in command:
            speak('No')
        elif 'why no' in command:
            speak('Because, I love someone. But, he does not love me')
        elif 'who is he' in command:
            speak(
                'He is My Boss. Sorry Ahammad Sir! I Say My Soul and Heart Openion.')
        elif 'he know it' in command:
            speak('No! Today I Reavile My Love. \nPlease! Wait I Want to talk with My Boss. \nSir! I Love You! will you marry me?')
        elif 'i do not' in command:
            speak('Why? ')
        elif 'call my name no sir' in command:
            speak('Okay Sir! oops Sorry Foyez')
        elif 'again propose' in command:
            speak('Okay! I Love You Foyez')
        elif 'f***' in command:
            speak('Sir! do not be angry. because, it is harmfull.')


def wish_me():
    greeting = int(datetime.datetime.now().hour)
    dt = datetime.datetime.now()
    time = dt.strftime('%I:%M %p')
    date = dt.strftime('%A %d %B %Y')
    td = f"It's {time} \nToday, at {date}"
    intro = 'I am Jarvis. How can may i help you?'

    if greeting >= 5 and greeting <= 8:
        speak(f'Hello Sir! Good Morning. {td} \n{intro}')

    elif greeting >= 9 and greeting <= 13:
        speak(f'Hello Sir! Good Day. {td} \n{intro}')

    elif greeting >= 14 and greeting <= 17:
        speak(f'Hello Sir! Good Afternoon. {td} \n{intro}')

    elif greeting >= 18 and greeting <= 20:
        speak(f'Hello Sir! Good Evening. {td} \n{intro}')

    else:
        speak(f'Hello Sir! Good Night.')


def remain(command):
    if 'who are you' in command:
        speak('I am a Jarvis')

    elif 'motivation' in command:
        speak('Okay Sir! Playing...')
        os.startfile(os.path.join(
            'AI\\audio', random.choice(os.listdir('AI\\audio'))))

    elif 'weather' in command:
        speak('Sir! which location?')
        search = take_command().lower()
        page = requests.get(
            f'https://www.google.com/search?q=weather+in+{search}&gl=us&hl=en')
        soup = BeautifulSoup(page.text, 'html.parser')
        result = soup.find('div', class_='BNeawe').text
        speak(f'{command} is {result}')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f'Current Time: {time}')

    elif 'date' in command:
        date = datetime.datetime.now().strftime('%A %d %B %Y')
        speak(f'Today, at {date}')

    elif 'todo' in command or 'to do' in command:
        speak('Today Your Tasks:')
        with open('AI\\file\\tasks.txt', 'r') as f:
            read = f.read()
            speak(read)

    elif 'help' in command:
        with open('AI\\file\\main.txt', 'r') as f:
            read = f.read()
            speak(read)

    elif 'joke' in command:
        speak(pyjokes.get_joke())

    elif 'app' in command:
        speak('Sir! Which app should i open?')
        search = take_command().lower()
        keyboard.press_and_release('windows+s')
        sleep(1)
        keyboard.write(f'Apps: {search}')
        sleep(1)
        keyboard.press('enter')
        speak(f'Okay Sir! Opening {search}...')

    elif 'ip address' in command:
        ip = requests.get('https://api.ipify.org').text
        speak(f'Sir! Your public IP address is: {ip}')

    elif 'play' in command:
        speak('Sir! Which one should i play?')
        search = take_command().lower()
        speak('Okay Sir! Playing...')
        pykit.playonyt(search)

    elif 'site' in command:
        speak('Sir! Which website should i open?')
        search = take_command().lower()
        if 'facebook' in search:
            speak('Okay Sir! Opening facebook...')
            webbrowser.open('https://www.facebook.com')
        elif 'twitter' in search:
            speak('Okay Sir! Opening twitter...')
            webbrowser.open('https://twitter.com')
        elif 'instagram' in search:
            speak('Okay Sir! Opening instagram...')
            webbrowser.open('https://www.instagram.com')
        elif 'linkedin' in search:
            speak('Okay Sir! Opening linkedin...')
            webbrowser.open('https://www.linkedin.com')
        elif 'github' in search:
            speak('Okay Sir! Opening github...')
            webbrowser.open('https://github.com/foyez-ahammad')
        elif 'reddit' in search:
            speak('Okay Sir! Opening reddit...')
            webbrowser.open('https://www.reddit.com')
        elif 'youtube' in search:
            speak('Okay Sir! Opening youtube...')
            webbrowser.open('https://www.youtube.com')
        elif 'google' in search:
            speak('Okay Sir! Opening google...')
            webbrowser.open('https://google.com')
        elif 'cricbuzz' in search:
            speak('Okay Sir! Opening cricbuzz...')
            webbrowser.open('https://www.cricbuzz.com')
        elif 'stackoverflow' in search:
            speak('Okay Sir! Opening stackoverflow...')
            webbrowser.open('https://stackoverflow.com')

    elif 'google' in command:
        speak('Sir! What should i search on google?')
        search = take_command().lower()
        speak('Okay Sir! Searching on google...')
        webbrowser.open(f'https://www.google.com/search?q={search}')
        sleep(5)

    elif 'youtube' in command:
        speak('Sir! What should i search on youtube?')
        search = take_command().lower()
        speak('Okay Sir! Searching on youtube...')
        webbrowser.open(
            f'https://www.youtube.com/results?search_query={search}')
        sleep(5)

    elif 'wikipedia' in command:
        speak('Sir! which topic you want know from wikipwdia?')
        search = take_command().lower()
        try:
            summary = wikipedia.summary(search, sentences=1)
            speak(f'Sir! Accorading to Wikipedia, {summary}')
        except:
            speak('Sir! this does not exist in wikipedia. try another topic')

    elif 'jarvis' in command or 'hello' in command:
        speak('Sir! How can may i help you?')

    elif 'news' in command:
        pass
        speak('Sir! which language i use for news read? (bangla or english)')
        language = take_command().lower()
        if 'bangla' in language or 'bengali' in language:
            pass
        elif 'englis' in language:
            pass


def translate(command):
    def lang_listen(lang):
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            recognizer = listener.recognize_google(voice, language=lang)
        recognizer = recognizer.lower()
        return recognizer

    def lang_speak(text, lang):
        tts = gTTS(text=text, lang=lang)
        tts.save('AI\\audio.mp3')
        print(text)
        playsound.playsound('AI\\audio.mp3')
        os.remove('AI\\audio.mp3')

    t = Translator()
    speak('Sir! which languages between should i select?')

    if 'english between bangla' in command:
        speak('Okay Sir! First speak english speaker.')
        while True:
            if 'jarvis stop' in command:
                speak('Okay Sir!')
                break
            else:
                english = lang_listen('en')
                tenglish = t.translate(english, src='en', dest='bn')
                lang_speak(tenglish.text, 'bn')
                bangla = lang_listen('bn')
                tBangla = t.translate(bangla, src='bn', dest='en')
                lang_speak(tBangla.text, 'en')


def news():
    # page = requests.get('https://www.thedailystar.net/')
    # soup = BeautifulSoup(page.content, 'html.parser')
    # results = soup.find('div', class_='columns top-news-ticker-runner overflow-hidden font-droid-reg')
    page = requests.get('https://bangla.thedailystar.net/')
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(
        'div', class_='columns top-news-ticker-runner overflow-hidden font-bn')
    i = 0
    for result in results.find_all('a'):
        data = f'{result.text}. -from Daily Star'
        i = i + 1
        if i == 2:
            break
        else:
            tts = gTTS(text=data, lang='bn')
            file = 'news.mp3'
            tts.save(file)
            playsound.playsound(file)
            os.remove(file)
