class Room:
    def __init__(self, name, lighting=None):
        if lighting is None:
            lighting = []
        self.name = name
        self.lighting = lighting
        