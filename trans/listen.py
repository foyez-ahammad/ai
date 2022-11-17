import speech_recognition as sr

listener = sr.Recognizer()


def en_listen():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            recognizer = listener.recognize_google(voice, language='en')
            recognizer = recognizer.lower()
            print(f'you: {recognizer}')
    except:
        return 'None'
    return recognizer


def bn_listen():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            recognizer = listener.recognize_google(voice, language='bn')
            recognizer = recognizer.lower()
            print(f'you: {recognizer}')
    except:
        return 'None'
    return recognizer
