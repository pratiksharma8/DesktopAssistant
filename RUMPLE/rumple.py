import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
browser = webbrowser.get('chrome')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning Pat!')
    elif 12 <= hour < 18:
        speak('Good Afternoon Pat!')
    else:
        speak('Good Evening Pat!')

    speak('I am Rumple!, How can I help you?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-US')
        print(f'You: {query}\n')

    except Exception:
        print('I am sorry, Say that again please...')
        speak('I am sorry, Say that again please...')
        return 'None'

    return query


if __name__ == '__main__':
    wishMe()

    running = True
    while running:
        query = takeCommand().lower()

        # Logic for executing task based on queries

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia,')
            print(results)
            speak(results)

        if 'open youtube' in query:
            browser.open('https://www.youtube.com/')

        if 'open google' in query:
            browser.open('https://www.google.com/')

        if 'open facebook' in query:
            browser.open('https://www.facebook.com/')

        if 'open instagram' in query:
            browser.open('https://www.instagram.com/')

        if 'open my website' in query:
            browser.open('https://pratikrajsharma.com/')

        if 'suraksha website' in query:
            browser.open('https://surakshyaghimire.com/')

        if 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(f'The time is {strTime}')
            speak(f'The time is {strTime}')

        if 'cancel' in query:
            running = False
