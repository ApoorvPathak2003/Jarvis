import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
import smtplib
import random
from googlesearch import search

master = 'Apoorv'

print('Initializing Tony...\nYour Desktop Assistant!!')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def Tony_speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    hour = datetime.datetime.now().hour

    if date == 7 and month == 2:
        Tony_speak('Happy Birthday' + master)

    if hour >= 0 and hour < 12:
        Tony_speak('Good Morning' + master)
    elif hour >= 121 and hour < 18:
        Tony_speak('Good Afternoon' + master)
    else:
        Tony_speak('Good Evening' + master)

    Tony_speak('Jarvis here. How can I help you?')

def send_email(send_email_to, email_content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('apoorvgunjanpathak@gmail.com', password)
    server.sendmail('apoorvnpathak@gmail.com', send_email_to, email_content)
    server.close()

def take_command():
    recognize = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening...')
        recognize.pause_threshold = 1
        audio = recognize.listen(source)
    
    try:
        print('Recognizing...')
        audio_query = recognize.recognize_google(audio, language = 'en-in')
        print(f'User said: {audio_query}')
    except Exception:
        Tony_speak('Sorry can not recognize. Please repeat again.')
        audio_query = None
    
    return audio_query

if __name__ == "__main__":
    Tony_speak('Initializing Tony. Your Desktop Assistant')
    greet()

    while True:

        audio_query = take_command()

        if 'wikipedia' in audio_query.lower():
            Tony_speak('Searching wikipedia...')
            query = audio_query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            Tony_speak(result)

        elif 'open youtube' in audio_query.lower():
            urL='https://www.youtube.com'
            chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(urL)

        elif 'open google' in audio_query.lower():
            urL='https://www.google.com'
            chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(urL)

        elif 'play music' in audio_query.lower():            
            songs_path = "C:\\Users\\apoor\\Music"
            songs = os.listdir(songs_path)
            random_number = random.randint(0, len(songs))
            os.startfile(os.path.join(songs_path, songs[random_number]))

        elif 'time' in audio_query.lower():
            time = datetime.datetime.now().strftime('%H:%M:%S')
            Tony_speak(f"{master} the time is {time}")

        elif 'open vs code' in audio_query.lower():
            code_path = "C:\\Users\\apoor\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\Visual Studio Code.lnk"
            os.startfile(code_path)

        elif 'send email' in audio_query.lower():
            Tony_speak("Make sure your email has has to unsecure apps. We won't harm your computer but it is necessary for proper functioning.")
            try:
                Tony_speak("What should I send?")
                email_content = take_command()
                send_email_to = 'apoorvnpathak@gmail.com'
                send_email(send_email_to, email_content)
                Tony_speak("Email send successfully!")
            except:
                Tony_speak("Sorry! Email can not be sent.")

        elif 'search in google' or 'google search' or 'search google' in audio_query.lower():
            Tony_speak('What do you want to search in google')
            search_query = take_command()
            try:
                chrome_path = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s'
                for url in search(search_query, tld = 'com', num = 1, stop = 1, lang = 'en', pause = 2):
                    webbrowser.open("https://google.com/search?q=%s" % search_query)
            except Exception as e:
                print('Sorry, error occured!!')
