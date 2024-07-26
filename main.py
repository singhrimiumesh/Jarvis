import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define the music library
musicLibrary = {
    "blinding lights": "https://www.youtube.com/watch?v=4NRXx6U8ABQ",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "dance monkey": "https://www.youtube.com/watch?v=q0hyYWKXF0Q",
    "levitating": "https://www.youtube.com/watch?v=TUVcZfQe-Kw",
    "someone like you": "https://www.youtube.com/watch?v=hLQl3WQQoQ0",
    "uptown funk": "https://www.youtube.com/watch?v=OPf0YbXqDm0",
    "despacito": "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
    "havana": "https://www.youtube.com/watch?v=HCjNJDNzw8Y",
    "rolling in the deep": "https://www.youtube.com/watch?v=rYEDA3JcQqw",
    "closer": "https://www.youtube.com/watch?v=PT2_F-1esPk"
}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open('http://google.com')
    elif "open youtube" in c:
        webbrowser.open('http://youtube.com')
    elif "open linkedin" in c:
        webbrowser.open('http://linkedin.com')
    elif "open instagram" in c:
        webbrowser.open('http://instagram.com')
    elif c.startswith("play "):
        song = c[len("play "):].strip()
        link = musicLibrary.get(song.lower())
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Hello, what can I do for you?")
                with sr.Microphone() as source:
                    print("Jarvis Activated...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
