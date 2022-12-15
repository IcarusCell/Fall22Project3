import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.loc = None
        self.has_passive = False
        self.has_active = False

    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def put_in_room(self, room):
        self.loc = room
        room.add_item(self)

class Flashlight(Item):
    def __init__(self, name, desc):
        super().__init__(name, desc)
        self.has_passive = True
    def passive_pickup(self, player):
        player.search_chance += 0.5
    def passive_drop(self, player):
        player.search_chance -= 0.5

class Medkit(Item):
    def __init__(self, name, desc):
        super().__init__(name, desc)
        self.has_active = True
    def activate(self, player):
        if player.wounded:
            input('You crack open the kit of medical supplies and bandage your open wound.')
            player.wounded = False
            return True
        input('You are not wounded, you cannot use the medkit.')
        return False
