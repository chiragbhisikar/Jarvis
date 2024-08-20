import requests
import speech_recognition as sr  # For Speach Recognition
import webbrowser
import pyttsx3  # For Text-To-Speach
import music_library
from retrieve_news import getArticles
from retrive_ai_generated import aiProcess

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(command):
    print("Command: ", command)
    # For Opening Google
    if "open google" in command.lower():
        webbrowser.open("http://www.google.com")
    # For Opening Linkedin
    elif "open linkedin" in command.lower():
        webbrowser.open("http://www.linkedin.com")
    # For Opening Facebook
    elif "open facebook" in command.lower():
        webbrowser.open("http://www.facebook.com")
    # For Opening Youtube
    elif "open youtube" in command.lower():
        webbrowser.open("http://www.youtube.com")
    # For Opening Instagram
    elif "open instagram" in command.lower():
        webbrowser.open("http://www.instagram.com")
    # For Play Song
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        print("Song: ", song)
        link = music_library.music[song]
        webbrowser.open(link)
    # For News Articles
    elif "news" in command.lower():
        articles = getArticles()
        for article in articles:
            # print(article["title"])
            speak(article["title"])
    # For AI Generated Response
    else:
        pass
        # aiProcess(command)
        # Let Us handle by chatgpt


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    # Listen For Wake Word
    while True:
        r = sr.Recognizer()
        print("recognizing")
        # recognize speech using Google Speech Recognition
        try:
            with sr.Microphone() as source:
                print("Listening!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Ya")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                processCommand(command)
        except Exception as e:
            print(format(e))
