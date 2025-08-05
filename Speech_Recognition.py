import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I'm your assistant. How can I help you?")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Speech recognition service is down.")
        return ""

def process_command(command):
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif "date" in command:
        date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {date}")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "play music" in command:
        music_dir = "C:/Users/Public/Music"  # Change this path
        songs = os.listdir(music_dir)
        if songs:
            speak("Playing music")
            os.startfile(os.path.join(music_dir, songs[0]))
        else:
            speak("No music files found.")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I don't understand. Please try again.")

# Main loop
if __name__ == "__main__":
    greet()
    while True:
        command = listen()
        if command:
            process_command(command)