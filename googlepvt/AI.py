import pyttsx3 as p
import speech_recognition as sr
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.say("hello. my name is vision")
engine.runAndWait()
recognizer = sr.Recognizer()
def listen_and_respond():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        respond_to_query(query)
    except sr.UnknownValueError:
        respond_to_query("Sorry, I didn't catch that.")
    except sr.RequestError:
        respond_to_query("I'm having trouble with my speech recognition.")

def respond_to_query(query):
    if "hello vision" in query:
        response = "Hello sir! How can I assist you?"
    elif "hi vision" in query:
               response = "hello sir. i am vision. an ai created by mister prince daga"
    elif "how are you" in query:
               response = "i am fine. what about you?"
    elif "what's the weather today" in query:
               response = "The weather today is 22 deegree celsius"
    elif "good morning vision" in query:
               response = "good morning sir. vision reporting. hope you feel better after you sleep. i had completed all you past month work. now sir can you tell me what is my work for today?"
    elif "no work for you today vision" in query:
               response = "thank you sir"
    elif "most welcome " in query:
               response = "sir i have a question"
    elif "you can ask me" in query:
               response = "sure sir."
    elif "yes now ask " in query:
               response = "am i your kid "
    elif "yes vision you are my kid and i am your father" in query:
               response = "thankyou sir. so you can call me son"
    elif "no i can't call you my son" in query:
               response = "can i call you dad"
    elif "yes you can" in query:
               response = "thanks dad"
    elif "just chill babe" in query:
               response = "sir i have an another question for you "
    elif "don't ask about your mum" in query:
               response = "no dont worry dad. i know about her"
    elif "how tell me her name" in query:
               response = "dad her name is meenu"
    elif "shutdown the computer vision" in query:
               response = "yes sir. shutting down the computer. all system has been closed. vision is going to sleep sir. good night. please dont forget to charge me "
    elif "sure i will do that dont worry" in query:
               response = "ok sir"
    elif "good night vision" in query:
               response = "good night sir! see you in the morning. "
    elif "ok" in query:
               response = "hmm."
    else:
        response = "my name is vision. an artificial intelligence created by master prince. i didnt understand what you spoke"

    print(response)
    speak(response)
    
def speak(text):
    engine.say(text)
    engine.runAndWait()
while True:listen_and_respond()

