from tkinter import *

class HomePage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Hello, this is the home page", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label_bottom = Label(self, text="Project done by @Nazar Kordiumov", font=self.controller.parameters_font)
        label_bottom.pack(side="bottom", pady=10)