# Python program to translate
# speech to text and text to speech
import speech_recognition as sr
import pyttsx3 

import os
from dotenv import load_dotenv
load_dotenv()

# get OPENAI KEY
OPENAI_KEY = os.getenv('OPENAI_KEY') 


import openai
openai.api_key = OPENAI_KEY


# Function to convert text to speech
def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Initialize the recogniser
r = sr.Recognizer()


def record_Text():
    # Loop in case of errors
        while(1):
            try:
                # use the mic as source of input
                with sr.Microphone() as source2:
                    
                    # Prepare recognizer to receive input
                    r.adjust_for_ambient_noise(source2, duration=0.2)

                    print("I'm listening")

                    # Listens for the user's input
                    audio2 = r.listen(source2)

                    # Using google to recognize audio
                    Mytext = r.recognize_google(audio2)
                    
                    # For debug porpuses
                    # print(Mytext)
                    
                    return Mytext

            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

            except sr.UnknownValueError:
                print("Unknown error ocurred")                 

def send_to_chatGPT(messages, model = "gpt-3.5-turbo"):
     
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5, 
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message

messages = [{"role":"user","content":"Please act like Cristiano Ronaldo"}]
while(1):
    text = record_Text()
    messages.append({"role":"user","content":text})
    response = send_to_chatGPT(messages)
    SpeakText(response)

    print(response)