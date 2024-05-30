# Main Programmer for this Class: Porcare, Dana E.
from tkinter import *  # Importing all classes and functions from tkinter module
from PIL import Image, ImageTk  # Importing Image and ImageTk classes from PIL module

class design_gui_interface():
    def frame_design(self, parent_frame, x, y, width_size, height_size, bg_color):
        self.frame = Frame(parent_frame, width=width_size, height=height_size, bg=bg_color)
        self.frame.place(x=x, y=y)
        return self.frame

    def label_design(self, parent_frame, x, y, text_value, bg_color, fg_color, font):
        self.label = Label(parent_frame, text=text_value, bg=bg_color, fg=fg_color, font=font)
        self.label.place(x=x, y=y)
        return self.label

    def entry_design(self, parent_frame, x, y, width_size, height_size, bg_color, fg_color, font, h_bg, h_color):
        self.entry = Entry(parent_frame, width=100, bg=bg_color, fg=fg_color, font=font, relief=SOLID, bd=1, highlightbackground=h_bg, highlightcolor=h_color, highlightthickness=0)
        self.entry.place(x=x, y=y, width=width_size, height=height_size)
        return self.entry

    def image1_design(self, parent_frame, x, y, image_location, width_size, height_size):
        self.image = Image.open(image_location)
        self.photo = ImageTk.PhotoImage(self.image.resize((width_size, height_size)))
        self.label = Label(parent_frame, image=self.photo, borderwidth=0)
        self.label.place(x=x, y=y)
        return self.image

    def image2_design(self, parent_frame, x, y, image_location, width_size, height_size):
        self.image = Image.open(image_location)
        self.photo = ImageTk.PhotoImage(self.image.resize((width_size, height_size)))
        self.label = Label(parent_frame, image=self.photo, borderwidth=0)
        self.label.place(x=x, y=y)
        return self.image

    def button_design(self, parent_frame, x, y, width_size, height_size, bg_color, fg_color, text_value, font):
        self.button = Button(parent_frame, text=text_value, bg=bg_color, fg=fg_color, font=font)
        self.button.place(x=x, y=y, width=width_size, height=height_size)
        return self.button

class AnimatedGIFLabel(Label):
    def __init__(self, master, path, *args, **kwargs):
        Label.__init__(self, master, *args, **kwargs)
        self.master = master
        self.path = path
        self.load_gif()
        self.show_frame()

    def load_gif(self):
        self.image = Image.open(self.path)
        self.frames = []
        try:
            while True:
                self.frames.append(ImageTk.PhotoImage(self.image.copy()))
                self.image.seek(len(self.frames))  # Move to the next frame
        except EOFError:
            pass  # End of the GIF reached
        self.image.seek(0)  # Reset the GIF to the first frame
        self.frame_index = 0
        return self.frames

    def show_frame(self):
        self.configure(image=self.frames[self.frame_index])
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.after(100, self.show_frame)  # Adjust the delay as needed
