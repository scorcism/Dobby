import pyttsx3
import datetime
import speech_recognition as sr



engine = pyttsx3.init()

voices = engine.getProperty('voices')
# print(voices[0])
engine. setProperty("rate", 172)
# engine=engine.setProperty("voice",voices[0].id)

# Text To speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish Function
def wish():
    time = int(datetime.datetime.now().hour)
    # print(time)
    if (time >= 12 and time <= 18):
        speak("Good AfterNoon ..")
    elif (time < 12 and time >=0):
        speak("Good Morning ..")
    else:
        speak("Good Evening")
    
    # speak("Dobby is here For you!! Tell me What you want From me..")

# Taking Commands from user function
def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        speak("Say Commands")
        # r.pause_threshold=0.8
        # r.energy_threshold = 200
        r.phrase_threshold = 0.1  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        r.non_speaking_duration = 0.3
        audio =r.listen(source)

        try:
            print("Recognising..")
            query = r.recognize_google(audio,lang="en-us")
            print("You said: " + query)
        
        except Exception as e:
            print(e)
            speak("Sorry I didn't get that. Please repeat again..")
            return "None"
    # return query



if __name__=="__main__":
    wish()
    commands()

