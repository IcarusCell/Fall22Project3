import random

import containers


class Room:
    rooms = []
    def __init__(self, description,tag = '', can_hide = False):
        self.desc = description
        self.monsters = []
        self.exits = []
        self.items = []
        self.searchable_items = []
        self.containers = []
        self.has_hiding_spots = can_hide
        self.tag = tag
        Room.rooms.append(self)
    def add_exit(self, exit_name, destination):
        self.exits.append([exit_name, destination])
    def get_destination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]
    def connect_rooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.add_exit(dir1, room2)
        room2.add_exit(dir2, room1)
    def exit_names(self):
        return [x[0] for x in self.exits]
    def add_item(self, item):
        self.items.append(item)
    def add_searchable_item(self, searchable_item):
        self.searchable_items.append(searchable_item)
    def remove_item(self, item):
        self.items.remove(item)
    def add_monster(self, monster):
        self.monsters.append(monster)
    def remove_monster(self, monster):
        self.monsters.remove(monster)
    def has_items(self):
        return self.items != []
    def get_item_by_name(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def has_monsters(self):
        return self.monsters != []
    def get_monster_by_name(self, name):
        for i in self.monsters:
            if i.name.lower() == name.lower():
                return i
        return False
    def random_neighbor(self):
        return random.choice(self.exits)[1]
    def add_container(self, name, desc):
        cont = containers.Container(name, desc, None, None)
        self.containers.append(cont)
    def has_containers(self):
        return len(self.containers) > 0
    def get_container_by_name(self, name):
        for i in self.containers:
            if i.name.lower() == name.lower():
                return i
        return False
    def remove_container(self, container):
        self.containers.remove(container)
