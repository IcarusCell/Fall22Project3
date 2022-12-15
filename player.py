import os

#------MENU-------
#- Drop Items
#   Implemented first. Adds the item back to the list of items in the room.

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.escape_room = None
        self.search_chance = 0.5
        self.wounded = False
        self.alive = True
        self.is_hidden = False
        self.previous_location = None
    # goes in specified direction if possible, returns True
    # if not possible returns False
    def go_direction(self, direction):
        new_location = self.location.get_destination(direction.lower())
        if new_location is not None:
            self.previous_location = self.location
            self.location = new_location
            self.is_hidden = False
            return True
        return False

    def pickup(self, item):
        if item.has_passive:
            item.passive_pickup(self)
        item.loc = self
        self.items.append(item)
        self.location.remove_item(item)
        self.is_hidden = False
    def open(self, container):
        print(f'From the {container.name} you grab:')
        self.is_hidden = False
        for i in container.items:
            print(i.name)
            i.loc = self
            if i.has_passive:
                i.passive_pickup(self)
            self.items.append(i)
        print()
        self.location.remove_container(container)

    def show_inventory(self):
        clear()
        print("You are currently carrying:")
        print()
        for i in self.items:
            print(i.name)
        print()
        input("Press enter to continue...")
    def attack_monster(self, mon):
        clear()
        print("You are attacking " + mon.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(mon.name + "'s health is " + str(mon.health) + ".")
        print()
        if self.health > mon.health:
            self.health -= mon.health
            print("You win. Your health is now " + str(self.health) + ".")
            mon.die()
        else:
            print("You lose.")
            self.alive = False
        print()
        input("Press enter to continue...")
    def drop_item(self, item):
        self.is_hidden = False
        for i,ent in enumerate(self.items):
            if ent.name.lower() == item.lower():
                self.location.items.append(ent)
                if ent.has_passive:
                    ent.passive_drop(self)
                self.items.remove(ent)
                return True
        return False
    def player_description(self):
        print('Current player status: ')
        print('- Health -')
        if self.wounded:
            print('Blood trickles from your open wound, you definitely need to find a way to patch yourself up.')
        else:
            print('You are feeling fine, though this place does put you on edge.')
        print('- Hiding -')
        if self.is_hidden:
            print('The cramped confines of your hiding space make you very uncomfortable, but it\'s better than facing what may be outside.')
        else:
            print('You are walking around in the open. Hopefully nothing can see you...')
    def activate_item(self, item):
        for i,ent in enumerate(self.items):
            if ent.name.lower() == item.lower():
                if ent.has_active:
                    if ent.activate(self):
                        if ent.has_passive:
                            ent.passive_drop(self)
                        self.items.remove(ent)
                        return True
        return False


