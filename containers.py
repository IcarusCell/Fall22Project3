import random
import os
import item

possible_items = []



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
class Container:
    def __init__(self, name, description, item=None, key_item=None):
        self.items = []
        if item == None:
            if len(possible_items) <= 2:
                num_items = 1
            else:
                num_items = random.randint(1, 2)
            for _ in range(num_items):
                key = random.randint(0,len(possible_items)-1)
                self.items.append(possible_items[key])
                del possible_items[key]
        else:
            self.items.append(item)
        if key_item == None:
            self.needs_key_item = False
        else:
            self.needs_key_item = True
            self.key_item = key_item
        self.name = name
        self.description = description
    def add_item(self, item):
        self.items.append(item)
    def describe(self):
        clear()
        print(self.description)
        print()
        input("Press enter to continue...")