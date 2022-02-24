# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 16:09:53 2022

This code is not mine and is frankenstiened from multiple sources.
"""
import pyglet, sys, os, time
from tkinter import filedialog

def animgif_to_ASCII_animation(animated_gif_path):
    # map greyscale to characters
    chars = ('#', '#', '@', '%', '=', '+', '*', ':', '-', '.', ' ')
    clear_console = 'CLS'

    # load image
    anim = pyglet.image.load_animation(animated_gif_path)

    # Step through forever, frame by frame
    while True:
        for frame in anim.frames:

            # Gets a list of luminance ('L') values of the current frame
            data = frame.image.get_data('L', frame.image.width)

            # Built up the string, by translating luminance values to characters
            outstr = ''
            for (i, pixel) in reversed(list(enumerate(data))):
                outstr += chars[int((pixel * (len(chars) - 1)) / 255)] + \
                          ('\n' if (i + 1) % frame.image.width == 0 else '')

            # Clear the console
            os.system(clear_console)

            # Write the current frame on stdout and sleep
            sys.stdout.write(outstr)
            sys.stdout.flush()
            time.sleep(0.1)

file_path = filedialog.askopenfilename()
# run the animation based on some animated gif
try:
    animgif_to_ASCII_animation(u''+file_path)
except KeyboardInterrupt:
    print('Later Tater...')
