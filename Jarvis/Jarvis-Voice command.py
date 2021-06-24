import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")

    speak("Please tell me how may I help you?")
    

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Say that again please...")  
        return "None"
    return query





if __name__ == "__main__":
    speak("Have a Good Day  ...!")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia ....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'song on spotify' in query:
            speak("Just Second ....")
            query = query.replace("song on spotify","")
            webbrowser.open('https://open.spotify.com/search/'+query)

        elif 'open youtube' in query:
            query = query.replace("open youtube","")
            webbrowser.open("https://www.youtube.com/results?search_query="+query)

        elif 'open google' in query:
            query = query.replace("open google","")
            webbrowser.open("https://www.google.com/search?q="+query)


        elif 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
                        

        elif 'Hello' in query:
            speak('Hello sir')

                
        elif 'Thank you' in query:
            speak("Welcome Mention not, Meet soon!")
            exit()
            
        elif 'Exit' in query:
            speak("Thanking you,Meet soon!")
            exit()
        elif 'stop' in query:
            speak("Thanking you, Meet soon!")
            exit()
            
    

        
