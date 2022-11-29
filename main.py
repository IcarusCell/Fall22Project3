from room import Room
from player import Player
from item import Item
from monster import Monster
import os
import updater

player = Player()

def create_world():

    #Nurse's Office
    nurse_office = Room("You enter a poorly lit, sterile feeling white room. \n Judging by the wax paper covered exam table and the various medications scattered across the floor, this is probably some sort of nurses office. \n To your south is the door you entered the room from.")
    north_hallway_1 = Room("You enter  another hallway flanked by row after row of lockers, all rusted with half the doors hanging off their hinges.\n To the north is a white door hanging on its hinges.\n To the east the hallway extends in a similar way. \n To the west the hallway curves southward, its extension escaping your view.")
    north_hallway_2 = Room("The hallway you walk through is similar to all the others. \n Numerous lockers against the walls alongside a wall of coat hangers where a fair few ragged coats flutter in the light wind that passes through this place. \n To the south is a pair of double doors with a large sign hanging above labeled 'CAFETERIA'. \n To the west the lockers continue along the walls, while to the east the hallway turns a corner. \n Finally, to the north, a wooden door with a sign labeled 'CLASSROOM 3A' stands closed.")
    cafeteria_1B = Room("You walk into the top right corner of the cafeteria. \n The wall is covered in a series of vending machines, all of which appear to be nonfunctional. \n To the north a set of double doors appear to lead out into a hallway. \n To the south the sprawling cafeteria continues onward to the area where orders appear to have been taken. \n To the west lies one end of the sprawling cafeteria tables where students used to enjoy their meals.")
    cafeteria_1A = Room("This area is filled with cafeteria tables, speckles of ominous looking gunk festering under the chairs. \n To the east the cafeteria continues into the vending machine area alongside a door that seems to lead outside. \n To the south lies the rest of the cafeteria tables, equally abandoned and covered in unknown substances.")
    a = Room("You are in room 1")
    b = Room("You are in room 2")
    c = Room("You are in room 3")
    d = Room("You are in room 4")

    Room.connect_rooms(nurse_office, 'south', north_hallway_1, 'north')
    Room.connect_rooms(north_hallway_1, 'east', north_hallway_2, 'west')
    Room.connect_rooms(cafeteria_1B, 'north', north_hallway_2, 'south')
    Room.connect_rooms(cafeteria_1A, 'east', cafeteria_1B, 'west')

    Room.connect_rooms(a, "east", b, "west")
    Room.connect_rooms(c, "east", d, "west")
    Room.connect_rooms(a, "north", c, "south")
    Room.connect_rooms(b, "north", d, "south")
    i = Item("Rock", "This is just a rock.")
    i.put_in_room(b)
    player.location = cafeteria_1A
    Monster("Bob the monster", 20, b)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_situation():
    clear()
    print(player.location.desc)
    print()
    if player.location.has_monsters():
        print("This room contains the following monsters:")
        for m in player.location.monsters:
            print(m.name)
        print()
    if player.location.has_items():
        print("This room contains the following items:")
        for i in player.location.items:
            print(i.name)
        print()
    print("You can go in the following directions:")
    for e in player.location.exit_names():
        print(e)
    print()

def show_help():
    clear()
    print("go <direction> -- moves you in the given direction")
    print("inventory -- opens your inventory")
    print("pickup <item> -- picks up the item")
    print("quit -- quits the game")
    print("drop <item> -- drops the item")
    print()
    input("Press enter to continue...")


if __name__ == "__main__":
    create_world()
    playing = True
    while playing and player.alive:
        print_situation()
        command_success = False
        time_passes = False
        while not command_success:
            command_success = True
            command = input("What now? ")
            if len(command) == 0:
                continue
            command_words = command.split()
            if len(command_words) == 0:
                continue
            match command_words[0].lower():
                case "go":   #cannot handle multi-word directions
                    okay = player.go_direction(command_words[1]) 
                    if okay:
                        time_passes = True
                    else:
                        print("You can't go that way.")
                        command_success = False
                case "pickup":  #can handle multi-word objects
                    target_name = command[7:] # everything after "pickup "
                    target = player.location.get_item_by_name(target_name)
                    if target != False:
                        player.pickup(target)
                    else:
                        print("No such item.")
                        command_success = False
                case "inventory":
                    player.show_inventory()
                case "help":
                    show_help()
                case "exit":
                    playing = False
                case "attack":
                    target_name = command[7:]
                    target = player.location.get_monster_by_name(target_name)
                    if target != False:
                        player.attack_monster(target)
                    else:
                        print("No such monster.")
                        command_success = False
                case "drop":
                    if player.drop_item(command_words[1]):
                        print(f"The {command_words[1]} tumbles into the dirt.")
                    else:
                        print(f"You do not have any {command_words[1]}")
                case other:
                    print("Not a valid command")
                    command_success = False
        if time_passes == True:
            updater.update_all()




