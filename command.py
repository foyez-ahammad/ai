from base import speak, take_command
from features import *


def commands():
    # wish_me()
    speak('i am active')
    while True:
        command = take_command().lower()

        if ('sleep' in command) or ('rest' in command) or ('hold' in command) or ('break' in command):
            speak('Okay Sir! i am going to sleep. you can call me anytime.')
            break

        elif 'talk' in command:
            talk()

        elif 'translat' in command:
            translate()

        elif 'f***' in command or 'what the heel' in command:
            speak('Sir! do not be angry. because, it is harmfull.')

        else:
            remain(command)
commands()
'''
def run():
    while True:
        command = take_command().lower()
        if 'wake' in command or 'hello' in command or 'jarvis' in command:
            commands()
        elif ('stop' in command) or ('done' in command) or ('bye' in command):
            speak('Thanks for using me. Have a good day.')
            break


run()
'''