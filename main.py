import speech_recognition as sr
from gtts import gTTS
import os

# initialize the recognizer
r = sr.Recognizer()

# set the minimum recording duration
MIN_RECORDING_DURATION = 5

# prompt the user to enter the recording duration
while True:
    try:
        duration = int(input(f"How long do you want to record (at least {MIN_RECORDING_DURATION} seconds)? "))
        if duration >= MIN_RECORDING_DURATION:
            break
        else:
            print(f"Please enter a value of at least {MIN_RECORDING_DURATION} seconds.")
    except ValueError:
        print("Please enter a valid integer.")

# use the default microphone as the source
with sr.Microphone() as source:
    print("Say something...")
    # listen for audio and store it in audio_data variable
    audio_data = r.record(source, duration=duration)
    print("Processing...")

# recognize speech using Google Speech Recognition
try:
    text = r.recognize_google(audio_data)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError:
    print("Sorry, my speech service is currently unavailable.")

# prompt the user to enter a file name to save the transcript
filename = input("Enter a file name to save the transcript (default is 'transcript.txt'): ")
if filename == "":
    filename = "transcript.txt"

# save the transcribed text to a file
with open(filename, "w") as file:
    file.write(text)

print(f"Transcript saved to '{filename}'.")

# ask the user if they would like the transcript to be read out loud
playback = input("Would you like me to read the transcript out loud? (y/n) ")
if playback == "y":
    # use Google Text-to-Speech to read the transcript out loud
    tts = gTTS(text)
    tts.save("transcript.mp3")
    os.system("start transcript.mp3")
elif playback == "n":
    print("Okay, no problem.")
else:
    print("Invalid input. Skipping playback.")
