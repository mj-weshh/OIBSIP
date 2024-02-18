# Voice Assistant

This Python script creates a simple voice assistant that can recognize speech commands and respond accordingly. It utilizes the SpeechRecognition library for speech recognition and the pyttsx3 library for text-to-speech conversion. The assistant can perform various tasks such as providing the current time, date, and performing web searches based on user commands.

## Features

- **Speech Recognition**: The script uses the SpeechRecognition library to recognize speech input from the user via the microphone.

- **Text-to-Speech Conversion**: It utilizes the pyttsx3 library to convert text responses into spoken audio.

- **Current Time and Date**: The assistant can provide the current time and date upon user request.

- **Web Search**: It can perform web searches using Google search based on user input.

## Requirements

- Python 3.x
- SpeechRecognition library (`pip install SpeechRecognition`)
- pyttsx3 library (`pip install pyttsx3`)
- webbrowser (standard library)

## Usage

1. Ensure that you have Python installed on your system.
2. Install the required libraries using pip.
3. Run the script using the command `python voice_assistant.py`.
4. Follow the prompts and speak your commands to the assistant.
5. You can say "exit" to terminate the program.

## Troubleshooting

- If the script is unable to recognize speech or encounter errors, ensure that your microphone is properly connected and configured.
- Make sure that the required libraries are installed correctly by running `pip list` in your terminal.

## Contributing

Contributions are welcome! If you encounter any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request on the GitHub repository.
