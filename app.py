import datetime
import os.path
import webbrowser

import openai
import pyttsx3
import speech_recognition as sr

from config import apikey

import streamlit as st

st.title("Jarvis AI Using OpenAI")


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        audio = r.listen(source)
        try:
            Query = r.recognize_google(audio, language="en-in")
            st.write(f'User Said : {Query}')
            return Query
        except Exception:
            return "Some Error Occurred."


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response : {prompt} \n ----------------------------------------------------------------\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # st.write(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    st.write(text)
    # if not os.path.exists("Openai"):
    #     os.mkdir("Openai")
    #
    # with open(f"Openai/{''.join(prompt.split('box')[1:]).strip()}.txt", "w") as f:
    #     f.write(text)


# Main Function


if st.button('Activate'):
    say("Jarvis Activate How Can I help you Sir")
    st.write("Listening...")
    while True:
        query = takeCommand()

        if query.lower().startswith("open"):
            website = query.split(" ", 1)[1]
            say(f"Opening {website} sir...")
            webbrowser.open(f"https://www.{website}.com")
            break

        elif "the time".lower() in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strTime}")
            st.write("Listening...")

        elif "using black box".lower() in query.lower():
            ai(prompt=query)
            break

        elif "time to leave".lower() in query.lower():
            say("See you again Sir...")
            break

        else:
            st.write("I don't understand sir.")
            say("I don't understand sir.")
            st.write("Listening...")
