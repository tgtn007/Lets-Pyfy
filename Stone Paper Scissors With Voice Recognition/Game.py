import random as rd
import pyttsx3
import speech_recognition as sr
b=['stone' , 'paper' , 'scissors']
i=1
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

rate=engine.getProperty("rate")
engine.setProperty("rate",95)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def reconiger():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recogniging...")
        ans=r.recognize_google(audio,language="en-IN")
        print(f"User --> {ans}")
        speak(f"User's choice is {ans}")
        if ans in b:
            return ans
        else:
            speak("Please try again, you are doing wrong pronunciation")
            reconiger()
    except:
        while i<=5:
            speak(f"say that again, assistant can not recognige your voice\n {5-i} trial left")
            reconiger()
            i=i+1
            return None
    return ans
def assistant():
    c=rd.choice(b)
    print(f"Computer --> {c}")
    speak(f"computer's choice is {c} ")
    return c
n=1
count=0
user=0
while n<=2:
    a=reconiger()
    x=assistant()
    if (x==b[0] and a==b[1]) or (x==b[1] and a==b[2]) or (x==b[2] and a==b[0]):
        count=count+1
    elif a==x:
        continue
    else:
        user=user+1
    n=n+1
if count<user:
    print("Assistant won")
    speak("Assistant won")
elif count>user:
    print("User won")
    speak("User won")
else:
    print("Match draw")
    speak("Match draw")


