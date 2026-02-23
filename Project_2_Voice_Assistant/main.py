import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit
import os

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
    except:
        command = ""
    return command


def run_assistant():
    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("Current time is " + time)

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "search" in command:
        topic = command.replace("search", "")
        speak("Searching for " + topic)
        pywhatkit.search(topic)

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 2)
        speak(info)

    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    elif "open notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")

    elif "exit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I did not understand.")


while True:
    run_assistant()
