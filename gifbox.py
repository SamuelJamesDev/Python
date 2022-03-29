# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 09:04:00 2022

@author: SamuelJames
"""
from tkinter import *
from tkinter import filedialog

def get_file():
    try:
        file_path = filedialog.askopenfilename()
        return (file_path)
        #img = Image.open(file_path)
    except AttributeError:
        print("no image chosen")
        exit()


class AnimatedGif(object):
    """ Animated GIF Image Container. """
    def __init__(self, image_file_path):
        # Read in all the frames of a multi-frame gif image.
        self._frames = []

        frame_num = 0  # Number of next frame to read.
        while True:
            try:
                frame = PhotoImage(file=image_file_path,
                                   format="gif -index {}".format(frame_num))
            except TclError:
                break
            self._frames.append(frame)
            frame_num += 1

    def __len__(self):
        return len(self._frames)

    def __getitem__(self, frame_num):
        return self._frames[frame_num]


def update_label_image(label, ani_img, ms_delay, frame_num):
    global cancel_id
    label.configure(image=ani_img[frame_num])
    frame_num = (frame_num+1) % len(ani_img)
    cancel_id = main.after(
        ms_delay, update_label_image, label, ani_img, ms_delay, frame_num)

def enable_animation():
    global cancel_id
    if cancel_id is None:  # Animation not started?
        ms_delay = 1000 // len(ani_img)  # Show all frames in 1000 ms.
        cancel_id = main.after(
            ms_delay, update_label_image, animation, ani_img, ms_delay, 0)

def cancel_animation():
    global cancel_id
    if cancel_id is not None:  # Animation started?
        root.after_cancel(cancel_id)
        cancel_id = None

def new_animation():
    global main
    for widget in main.winfo_children():
        widget.destroy()

    root = Tk()
    main=Frame(root)
    main.pack()
    root.title("Animation Demo")
    root.geometry("700x600+100+100")
    runme = get_file()
    ani_img = AnimatedGif(runme)
    cancel_id = None

    animation = Label(image=ani_img[0])  # Display first frame initially.
    animation.pack()
    Button(root, text="start animation", command=enable_animation).pack()
    Button(root, text="stop animation", command=cancel_animation).pack()
    Button(root, text="exit", command=root.quit).pack()
    Button(root, text="Choose new Image", command=root.quit).pack()

try:
    root = Tk()
    main = Frame(root)
    root.title("Animation Demo")
    root.geometry("700x600+100+100")
    runme = get_file()
    ani_img = AnimatedGif(runme)
    cancel_id = None

    animation = Label(image=ani_img[0])  # Display first frame initially.
    animation.pack()
    Button(root, text="start animation", command=enable_animation).pack()
    Button(root, text="stop animation", command=cancel_animation).pack()
    Button(root, text="exit", command=root.quit).pack()
    Button(root, text="Choose new Image", command=new_animation).pack()

    root.mainloop()
except KeyboardInterrupt:
    print("goodbye!")
