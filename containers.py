import random
import os
import item

possible_items = []



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
class Container:
    def __init__(self, name, description, item=None, key_item=None, poss_items = None):
        self.items = []
        if item == None and poss_items == None:
            num_items = random.randint(1,3)
            for _ in range(num_items):
                self.items.append(possible_items[random.randint(0,len(possible_items)-1)])
        elif item==None and poss_items != None:
            num_items = random.randint(1,3)
            for _ in range(num_items):
                self.items.append(poss_items[random.randint(0,len(poss_items)-1)])
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