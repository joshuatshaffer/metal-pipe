#!/usr/bin/python3

"""
Play the falling metal pipe sound effect when the pipe character is typed.
"""

from pynput.keyboard import Key, Listener
from playsound import playsound
 
def on_press(key):
    try:
        if key.char == "|":
            # TODO: Make this play faster. There is a delay between key press and sound.
            playsound("Destruction_Metal_Pole_L_Wave_2_0_0.wav", False)
    except:
        pass
 
with Listener(on_press=on_press) as listener:
    listener.join()
