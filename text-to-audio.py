#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rahul
"""

from gtts import gTTS
from pydub import AudioSegment
# play the converted audio
import os

# Define the text to be converted to speech
text = "Hello world!"


# Define the language
language = "en"

# Create a gTTS object
tts = gTTS(text=text, lang=language, slow=False)

# Save the speech as an MP3 file
tts.save(" filename .mp3")

# Load the background music audio
music = AudioSegment.from_file('music file name .mp3')

# Load the gTTS audio
audio = AudioSegment.from_file('filename.mp3')

# Mix the two audio files together
mixed_audio = music.overlay(audio, loop=True)

# Export the mixed audio to an MP3 file
mixed_audio.export('mixedfilename.mp3', format='mp3')

# Playing the converted file
os.system("mpg321 mixedfilename.mp3")
