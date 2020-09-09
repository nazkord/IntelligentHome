class Light():
    def __init__(self, name, location, power=False, brightness=50, colors=None):
        self.name = name
        self.location = location
        self.power = power
        self.brightness = brightness
        self.colors = []
        self.current_color = None

        if colors:
            self.colors = colors
            self.current_color = colors[0]


    def change_power(self):
        self.power = not self.power


    def power_button_text(self):
        if not self.power:
            return 'ON'
        else:
            return 'OFF'


    def power_button_color(self):
        if self.power:
            return 'red'
        else:
            return 'green'


    def change_brightness(self, value):
        self.brightness = value


    def change_color(self, value):
        self.current_color = value


    def color_number(self):
        for i, color in enumerate(self.colors):
            if self.current_color == color:
                return i
        return 0