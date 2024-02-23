#importing necessary modules
 
import os
import speech_recognition as sr


# Creating  a recognizer instance
r = sr.Recognizer()

# recording the audio and Recognizing the audio file
with sr.Microphone() as source:
    print()
    print()
    print("Recording audio")
    audio = r.listen(source)

# Converting  the given audio to text
text = r.recognize_google(audio)
print()
print()
print("The recorded audio: ",text)

#translating the given speech
from googletrans import Translator
translator = Translator()
x=translator.translate( text, dest='ur')
trns_text=x.text


#translating text to speech using gtts
from gtts import gTTS

# Specifying the language
language = 'ur'

# Creating a gTTS object
tts = gTTS(trns_text, lang=language, slow=False)
# Saving  the speech as an audio file to play afterwards
tts.save("urdu_speech.mp3")
# Playing the saved audio file which plays the translated audio
os.system("start urdu_speech.mp3")
