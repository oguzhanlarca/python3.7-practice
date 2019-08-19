#!/usr/bin/python3
""" Instrument by Barron Stone for Code Clinic: Python """
from tkinter import *
from tkinter import ttk
import numpy as np
import simpleaudio as sa

SAMPLE_RATE = 44100 # Hz
DURATION = 60 # max seconds to hold any tone
TIME_VECT = np.linspace(0, DURATION, DURATION * SAMPLE_RATE, False) # time vector for audio

class Instrument:

    def __init__(self, master):
        # register handlers for mouse events
        master.bind('<Motion>', self._mouse_move)
        master.bind('<ButtonPress>', self._mouse_down)
        master.bind('<ButtonRelease>', self._mouse_up)
        master.bind('<Escape>', lambda e: master.destroy())
        self.prev_mouse_event = None # used to track mouse movements

        # draw the canvas
        master.attributes('-fullscreen', True)
        self.canvas = Canvas(master, background='black')
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.create_text(master.winfo_screenwidth()//2, master.winfo_screenheight(),
                                anchor='s', text="Press 'Esc' to Quit.",
                                font=('Helvetica', 32, 'bold'), fill='white')

    def _mouse_move(self, event):
        # update canvas color
        R = int(255 * event.x / self.canvas.winfo_width() * (self.canvas.winfo_height() - (event.y + 1)) / self.canvas.winfo_height())
        B = int(255 * event.x / self.canvas.winfo_width() * (event.y + 1) / self.canvas.winfo_height())
        self.canvas.config(background = '#{:02x}30{:02x}'.format(R, B)) # set green to 0x30 for a "bit o' pizzazz"

        if self.prev_mouse_event: # mouse is down
            self.canvas.create_line(self.prev_mouse_event.x, self.prev_mouse_event.y,
                                    event.x, event.y, width = 10,
                                    fill = '#{:02x}88{:02x}'.format(R, B))
            self._play_sound(event.x, event.y)
            self.prev_mouse_event = event

    def _mouse_down(self, event):
        self._play_sound(event.x, event.y)
        self.prev_mouse_event = event

    def _mouse_up(self, event):
        sa.stop_all()
        self.canvas.delete('all')
        self.canvas.create_text(self.canvas.winfo_width()//2, self.canvas.winfo_height(),
                                anchor = 's', text="Press 'Esc' to Quit.",
                                font = ('Helvetica', 32, 'bold'), fill='white')
        self.prev_mouse_event = None

    def _play_sound(self, x_pos, y_pos):
        # calculate frequency of "piano key" based on y_pos
        pkey = np.floor(88 * (self.canvas.winfo_height() - (y_pos + 1)) / self.canvas.winfo_height() + 1)
        frequency =  440 * 2**((pkey - 49)/12) # 440Hz is key #49 on a piano

        # calculate volume based on x_pos
        volume = x_pos / self.canvas.winfo_width()

        # generate and play audio samples
        audio = np.round(np.sin(frequency * TIME_VECT * 2 * np.pi))
        audio *= volume * 32767
        audio = audio.astype(np.int16)
        sa.stop_all()
        sa.play_buffer(audio, 1, 2, SAMPLE_RATE)

def main():
    root = Tk()
    gui = Instrument(root)
    root.mainloop()

if __name__ == "__main__": main()
