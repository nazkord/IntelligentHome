from tkinter import *
from tkinter import font as tkfont
from UI.roomPage import *
from UI.homePage import *
from configParser import Config_Parser 
FILE_CONFIG_PATH = 'pilotConfig.json'


class Pilot(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title("Pilot")
		#creating fonts for the whole application
		self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
		self.listbox_font = tkfont.Font(family='Helvetica', size=16, slant="italic")
		self.parameters_font = tkfont.Font(family='Helvetica', size=17, slant="italic")
		self.geometry("600x700")

		#creating a main Frame - container for others pages (frames)
		self.container = Frame(self)
		self.container.pack(side="top", fill="both", expand=True)
		self.container.grid_rowconfigure(0, weight=1)
		self.container.grid_columnconfigure(0, weight=1)

		self.read_config_file(FILE_CONFIG_PATH)
		self.create_menubar()

		#creating HomePage and then show it
		self.frames = {}
		self.frames["HomePage"] = HomePage(self.container, self)
		self.frames["HomePage"].grid(row=0, column=0, sticky="nsew")

		self.show_frame("HomePage")


	def create_menubar(self):
		menubar = Menu(self)

		for item in self.rooms:
			menubar.add_command(label=item, command=lambda item=item: self.display_room(item))
		menubar.add_command(label="exit", command=self.quit)

		self.configure(menu=menubar)


	def read_config_file(self, file_config_path):
		self.parser = Config_Parser(file_config_path)
		self.rooms = self.parser.rooms


	#create and display room frame by its name
	def display_room(self, roomName):
		room = self.rooms.get(roomName)
		self.frames[roomName] = RoomPage(self.container, self, room)
		self.frames[roomName].grid(row=0, column=0, sticky="nsew")

		self.show_frame(roomName)


	#show a frame for the given page name
	def show_frame(self, page_name):		
		frame = self.frames[page_name]
		frame.tkraise()
