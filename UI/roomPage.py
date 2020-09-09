from tkinter import *
from tkinter import ttk
from mqtt.publisher import Publisher

class RoomPage(Frame):

    def __init__(self, parent, controller, room):
        Frame.__init__(self, parent)
        self.controller = controller
        self.room = room
        self.lighting = self.room.lighting
        self.publisher = Publisher()

        label = Label(self, text=('You are in the %s. Select one of the lights:' %self.room.name), font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the home page", command=lambda: controller.show_frame("HomePage"))
        button.pack(side="bottom", pady=20)

        #listbox of lights
        self.create_listbox()


    def create_listbox(self):
        light_listbox = Listbox(self, width=35, height=8,font=self.controller.listbox_font)
        light_listbox.pack(pady=10)
        for light in self.lighting:
                light_listbox.insert(0, light)
        light_listbox.bind('<<ListboxSelect>>', self.onselect)        


    def onselect(self, evt):
        # Clear all widgets for previous light
        children = self.winfo_children()
        for i in range(3, len(children)):
            children[i].destroy()

        # Tkinter passes an event object to onselect() from which we can get the selected value from list box
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.light = self.lighting.get(value)
        self.light_name_label = Label(self, text=('Light: %s' %self.light.name), font=self.controller.title_font)
        self.light_name_label.pack()
        self.setting_power()                     # do not display light config UI when the light is off
        if self.light.power:
            self.setting_brightness()
            if self.light.current_color:         # do not display UI when there is no color option for light
                self.setting_colors()


    #UI for power parameter
    def setting_power(self):
        self.power_label = Label(self, text='Power:', font=self.controller.parameters_font)
        self.power_label.pack(pady=10)
        self.power_button = Button(self, text=('Turn %s' %self.light.power_button_text()), 
                command=lambda: self.publisher.publish(self.light.location + "/power", self.light.power_button_text()),
                # command=lambda: self.light.change_power(),
                foreground=self.light.power_button_color())
        self.power_button.pack()


    #UI for brightness parameter
    def setting_brightness(self):
        self.brightness_label = Label(self, text='Brightness:', font=self.controller.parameters_font)
        self.brightness_label.pack(pady=10)
        self.brightness_scale = Scale(self, from_=0, to=100, orient=HORIZONTAL)
        self.brightness_scale.set(self.light.brightness)
        self.brightness_scale.pack()
        self.brightness_button = Button(self, text='Change', 
            command=lambda: self.publisher.publish(self.light.location + "/brightness", self.brightness_scale.get()))
            # command=lambda: self.light.change_brightness(self.brightness_scale.get()))
        self.brightness_button.pack(pady=3)


    #UI for color parameter
    def setting_colors(self):
        self.color_label = Label(self, text='Color:', font=self.controller.parameters_font)
        self.color_label.pack(pady=10)
        self.color_combobox = ttk.Combobox(self, state='readonly')
        self.color_combobox['values'] = self.light.colors
        self.color_combobox.current(self.light.color_number())
        self.color_combobox.pack(pady=3)
        self.color_button = Button(self, text='Change',
            command=lambda: self.publisher.publish(self.light.location + "/color", self.color_combobox.get()))
            # command=lambda: self.light.change_color(self.color_combobox.get()))
        self.color_button.pack(pady=3)
