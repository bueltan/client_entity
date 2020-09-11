# import PyOpenAL (will require OpenAL32.dll)

from openal import *

# import the time module, for sleeping during playback

import time

# open our wave file

source = oalOpen("Ensoniq-ZR-76-01-Dope.wav")

# and start playback

source.play()

# check if the file is still playing

while source.get_state() == AL_PLAYING:
    # wait until the file is done playing

    time.sleep(1)

# release resources (don’t forget this)

oalQuit()
