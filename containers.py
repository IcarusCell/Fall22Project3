import random

import item

possible_items = []


class Container:
    def __init__(self, name, description, item=None, key_item=None):
        self.items = []
        if item == None:
            num_items = random.randint(0,3)
            for _ in range(num_items):
                self.items.append(possible_items[random.randint(0,len(possible_items)-1)])
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