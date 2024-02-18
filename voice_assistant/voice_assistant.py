import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Can you repeat?")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

# Function to perform actions based on user commands
def process_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        speak("What do you want me to search?")
        search_query = listen()
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
    else:
        speak("Sorry, I didn't understand that command.")

# Main function to run the voice assistant
def main():
    speak("Hello! I'm your voice assistant. How can I help you?")
    
    while True:
        command = listen()
        if command == "exit":
            speak("Goodbye!")
            break
        process_command(command)

if __name__ == "__main__":
    main()
