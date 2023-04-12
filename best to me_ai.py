#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rahul
"""

from gtts import gTTS
from pydub import AudioSegment
# play the converted audio
import os
#%%
# Define the text to be converted to speech
text = """

I have a dream
That's all I need
I'll make it happen with some work and belief
Know what I want
So I'll take it on
I've made mistakes but mistakes make you strong

Let's break it down for a minute
I want the crown I'm gon get it
You hear me loud man I'm winning
Yea Charley Sheen would be grinning
These ladies know that I'm sinning
And this is just the beginning
I'm closing in the 9th inning
There ain't no point in resisting

Livin' life
Like a dream
Live it right
That's the theme
Every night
Got a team
Mobbing tight
To the scene
Out on stage
Hear em scream
Ok, this the dream
And I prayed
As a teen
One day
It'd be me
If I want it
Then I get it
Head down
Don't regret it
Push myself
To the limit
If I play it
Then I win it
I'm just saying
I'm just living
For today
For a minute
I don't stay
I just visit
Have no shame
I'll admit it yea

They're lookin' right at me
To see if I succeed
To see if I believe
They're looking up to me
They want the best of me now
Best of me now
Best of me now
Best of me
They want the best of me now
Best of me now
Best of me now
Best of me

And I won't rest in piece now
Rest in peace now
Rest in peace now
Rest in peace now

They want it now...
They want it now...
They want it now...
They want it now...
They want it now...
They want it now...
Oh damn if they want it now they got it now!

I swear to god man Ima make it soon
Silence all the haters as they see us making moves
I do what I want so I got nothing to prove
Stayin' motivated teaching others what to do

I'm staying focused
My mind is open
They start to notice
That I'm in motion
There is no potion
Your not just chosen
It takes devotion
To stay composed man

Never stop never stall
There ain't no time to fall
Try to live get it all
You got one life to ball
Thinking big never small
Cuz you gotta want it all
When you finally get that call
You get ready take it all

I don't need a handout
I already standout
Startin' to advance now
Ready to expand now
You don't have a chance now
Cuz we're in demand now
Make it by the grand now
Feelin' in command now

They're lookin' right at me
To see if I succeed
To see if I believe
They're looking up to me
They want the best of me now
Best of me now
Best of me now
Best of me
They want the best of me now
Best of me now
Best of me now
Best of me

They want the best of me now
Best of me now
Best of me now
Best of me

And I won't rest in piece now
Rest in peace now
Rest in peace now
Rest in peace now

They want it now...
They want it now...
They want it now...
They want it now...
They want it now...
Oh damn if they want it now they got it now!

"""

# Define the language
language = "en"

# Create a gTTS object
tts = gTTS(text=text, lang=language, slow=False)

# Save the speech as an MP3 file
tts.save("best to me.mp3")

# Load the background music audio
music = AudioSegment.from_file('NEFFEX_BEST_OF_ME_INSTRUMENTAL.mp3')

# Load the gTTS audio
audio = AudioSegment.from_file('best to me.mp3')

# Mix the two audio files together
mixed_audio = music.overlay(audio, loop=True)

# Export the mixed audio to an MP3 file
mixed_audio.export('NEFFEX_BEST_OF_ME.mp3', format='mp3')

# Playing the converted file
os.system("mpg321 NEFFEX_BEST_OF_ME.mp3")