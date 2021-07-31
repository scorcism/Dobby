import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# text to speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Applications Path
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
spotifypath= "C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk"
codePath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"


#For Some Normal Talk With dobby
def dobbySpeak():
    dobby_there = ["Always at your service sir", "Yes Sir", "Always!", "Yes Sir, I Love Seeing you work"]
    dobby_there_speak = random.choice(dobby_there)
    speak(dobby_there_speak)

def dobbyLoveYou():
    dobby_love = ["I Love You 3000 Sir", "I Love you too!", "yeah Sir Love You Too!","aapka aabhar sir"]
    dobby_love_speak = random.choice(dobby_love)
    speak(dobby_love_speak)

# Greeting message
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening Sir!")  

    speak("Hello Sir dobby's Here to Help You!")       

#  function
def takeCommand():
    print("Listening..")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Microphone...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source=source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, "\n")
        print(f"User said: {query}\n")

    except:   
        print("Say that again please...")  
        speak("Can't hear you sir, say that again!")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    takeCommand()

    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'shutdown' in query:
            speck("shutdown will begin in 3 seconds")
            speck("2")
            speck("1")
            quit(speak ('Shutting Down.... Good Bye Sir'))

        elif 'open youtube' in query:
            try:
                speak("opening youtube")
                webbrowser.get(chrome_path).open("youtube.com")
            except:
                speak("opening youtube")
                webbrowser.open("youtube.com")

        elif 'open google' in query:
            try:
                speak("opening google")
                webbrowser.get(chrome_path).open("google.com")
            except:
                speak('opening Google')
                webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            try:
                speak("opening stackoverflow")
                webbrowser.get(chrome_path).open("stackoverflow.com")
            except:
                speak('opening stackoverflow')
                webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            try:
                speak("opening facebook")
                webbrowser.get(chrome_path).open("facebook.com")
            except:
                speak("opening facebook")
                webbrowser.open("facebook.com")

        elif 'open twitter' in query:
            try:
                speak("opening twitter")
                webbrowser.get(chrome_path).open("twitter.com")
            except:
                speak("opening Twitter")
                webbrowser.open("twitter.com")

        elif 'play music' in query:
            try:
                os.startfile(spotifypath)
                speak('Playing Music!')
            except:
                speak("Sir Please Install Sptify First!")
                webbrowser.open("https://www.spotify.com/in/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            try:
                os.startfile(codePath)
            except:
                speak("Please Install VSCode First!")
                webbrowser.open("https://code.visualstudio.com/")

        elif 'who made you' in query:
            speak("Abhishek and  Rohan are The Creator Of Me! I Love Them 3000!")
        
        elif 'you there' in query:
            dobbySpeak()
        
        elif 'love you' in query:
            dobbyLoveYou()
