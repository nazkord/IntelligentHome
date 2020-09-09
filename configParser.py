import json
from objects.room import Room
from objects.lighting import Light

class Config_Parser:
    def __init__(self, file_config_path):
        self.rooms = self.read_rooms(file_config_path)      #reading rooms from json file


    def read_rooms(self, file_config_path):
        roomJson = json.load(open(file_config_path))
        rooms = dict()                                      #dict where rooms will be stored

        for room in roomJson:                               #create room and for each create dict of lights
            rooms[room['name']] = Room(room['name'], self.read_lighting_for(room))

        return rooms


    def read_lighting_for(self, room):
        lights = dict()                 #creating dict of lights and combining topic name for each

        for light in room['lighting']:
            lights[light['name']] = Light(light['name'],
                str('room/' + room['name'] + '/light/' + light['name']),
                colors=light['colors'])
        return lights
