# Text_and_Speech

The code is a Python program that uses the SpeechRecognition library to transcribe audio input from the user's microphone, saves the transcribed text to a file, and optionally reads it aloud using Google Text-to-Speech. The user is prompted to enter the duration of the audio recording, and the minimum length is set to 5 seconds. Once recorded, the audio data is passed to the Google Speech Recognition API and the transcribed text is printed to the console and saved to a file with a user-specified file name or the default file name "transcript.txt". The program then prompts the user to choose whether to read the transcript aloud, and if so, the program uses gTTS to convert the text to an mp3 file and open it for playback. Finally, the user is prompted to choose whether to translate the transcript into another language, but this feature has been removed at your request. The updated code will also prompt the user for a name for the transcript.mp3 file if they choose to play it.