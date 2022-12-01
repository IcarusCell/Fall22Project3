from room import Room
from player import Player
from item import Item
import random
from monster import Monster
import os
import updater

#------MENU-------
#- Drop Items(1)
#   Implemented first. Adds the item back to the list of items in the room.
#- Map Expansion(2)
#   Implemented, to be expanded upon as the game develops. Game takes place in a school, central area is 4x4 with several rooms branching off.
#- Search function(3)
#   Allows the player to effectively take a turn off in order to search a room for an item that may not be on the items list already.
#- Intro statement(1)
#   Introduces the player to the concept of the game and various features
#- Wait function(1)
#   Allows the player to wait for 1 turn worth of time
#- Hide function
#   Allows the player to hide from the monster for one turn
#- Containers
#   Complex new object type. Allows for randomization and keys. Store multiple items that the player can collect.
player = Player()

def create_world():

    #Nurse's Office, connects to north_hallway_B.
    nurse_office = Room("You enter a poorly lit, sterile feeling white room. \n Judging by the wax paper covered exam table and the various medications scattered across the floor, this is probably some sort of nurses office. \n To your south is the door you entered the room from.")

    #Two hallway tiles in the north zone of the map
    north_hallway_A = Room("You enter a hallway flanked by row after row of lockers, all rusted with half the doors hanging off their hinges.\n To the north is a white door hanging on its hinges.\n To the east the hallway extends in a similar way. \n To the west the hallway curves southward, its extension escaping your view.")
    north_hallway_B = Room("The hallway you walk through is similar to all the others. \n Numerous lockers against the walls alongside a wall of coat hangers where a fair few ragged coats flutter in the light wind that passes through this place. \n To the south is a pair of double doors with a large sign hanging above labeled 'CAFETERIA'. \n To the west the lockers continue along the walls, while to the east the hallway turns a corner. \n Finally, to the north, a wooden door with a sign labeled 'CLASSROOM 3A' stands closed.")

    top_right_corner = Room('You walk through the north eastern corner of the school. \n Lockers follow the left wall while benches sparsely occupy the right. \n To the west and south the rows of lockers extend out into the fog.')
    top_left_corner = Room('You walk through the north western corner of the school. \n Lockers follow the left wall while benches sparsely occupy the right. \n To the east and south the rows of lockers extend out into the fog.')

    east_hallway_A = Room('You step into a lengthy hallway with mist clinging to the floor like a dense web. \n Rusty lockers flank you on your left and right. \n To the south the hallway continues onward while to the north the hallway turns toward the west.')
    east_hallway_B = Room('This section of the hallway is just as dreary as the rest of this place. \n Mist obscures your vision and all you are able to see are the few benches to your left where students were likely supposed to wait for class. \n To the north the hallway continues onward, while to the south it turns a corner heading westward.')

    west_hallway_A = Room('The school\'s cracked bricks extend forward until they vanish out of sight, covered by the mist. \n To the north you can make out a turn in the hallway heading eastward, while to the south this path continues straight onward.')
    west_hallway_B = Room('The hallway you enter, although filled with lockers on the right wall, also contains a few vending machines that appear to be completely non-functional. \n To the north the hallway appears to continue onward in a straight line, although the mist makes it hard to tell. \n To the south the hallway curves eastward seeming to connect back to the front door.')

    south_hallway_A = Room('Your steps echo through this mist filled hallway. \n The white fluorescent lights periodically spark ominously overhead. \n The thick mist that permeates the school makes it hard to see, but to the west the hallway appears to bend towards the northern part of the school. \n To the east the hallway proceeds in a straight line.')
    south_hallway_B = Room('You enter a hallway, rust covering encrusting the hinges of every locker shoddily propped up against the brick walls. \n To the west the lockers vanish into the misty hallway, continuing in a straight line. \n To the east the hallway appears to turn the corner, leading up towards the northern section of the school.')

    bottom_left_corner = Room('You walk through the south western corner of the school. \n Lockers follow the left wall while benches sparsely occupy the right. \n To the east and north the rows of lockers extend out into the fog.')
    bottom_right_corner = Room('You walk through the south eastern corner of the school. \n Lockers follow the left wall while benches sparsely occupy the right. \n To the west and north the rows of lockers extend out into the fog.')

    #Cafeteria zone, central four squares of the map. Open space where each square can see each other.
    cafeteria_1B = Room("You walk into the top right corner of the cafeteria. \n The wall is covered in a series of vending machines, all of which appear to be nonfunctional. \n To the north a set of double doors appear to lead out into a hallway. \n To the south the sprawling cafeteria continues onward to the area where orders appear to have been taken. \n To the west lies one end of the sprawling cafeteria tables where students used to enjoy their meals.")
    cafeteria_1A = Room("This area is filled with cafeteria tables, speckles of ominous looking gunk festering under the chairs. \n To the east the cafeteria continues into the vending machine area alongside a door that seems to lead outside. \n To the south lies the rest of the cafeteria tables, equally abandoned and covered in unknown substances and a pair of double doors that appear to lead out into the main corridor.")
    cafeteria_2A = Room("You enter the bottom left corner of the cafeteria. \n Long, pale blue cafeteria tables flanked by chairs extend through the whole room up toward the top left corner of the cafeteria. \n To the east you see the buffet style area where orders seem to have been taken. \n To your south lie a set of double doors that seem to lead out into the primary school corridor.")
    cafeteria_2B = Room("As you walk into the bottom right corner of the cafeteria, the scent of rotting food hits you with staggering force. \n Pounds of rotting food seem to lie within the buffet style counter, it seems that no one cleaned it out after the school shut down. \n To the north is the vending machine section of the cafeteria alongside a set of doors that lead out into the north hallway. \n To the east is one end of the long cafeteria tables alongside another set of doors leading to the southern side of the school.")

    #Connecting the ring of hallways
    Room.connect_rooms(north_hallway_A, 'east', north_hallway_B, 'west')
    Room.connect_rooms(north_hallway_B, 'east', top_right_corner, 'west')
    Room.connect_rooms(top_right_corner, 'south', east_hallway_A, 'north')
    Room.connect_rooms(east_hallway_A, 'south', east_hallway_B, 'north')
    Room.connect_rooms(east_hallway_B, 'south', bottom_right_corner, 'north')
    Room.connect_rooms(bottom_right_corner, 'west', south_hallway_B, 'east')
    Room.connect_rooms(south_hallway_B, 'west', south_hallway_A, 'east')
    Room.connect_rooms(south_hallway_A, 'west', bottom_left_corner, 'east')
    Room.connect_rooms(west_hallway_B, 'south', bottom_left_corner, 'north')
    Room.connect_rooms(west_hallway_A, 'south', west_hallway_B, 'north')
    Room.connect_rooms(west_hallway_A, 'north', top_left_corner, 'south')
    Room.connect_rooms(top_left_corner, 'east', north_hallway_A, 'west')




    Room.connect_rooms(nurse_office, 'south', north_hallway_A, 'north')
    Room.connect_rooms(cafeteria_1B, 'north', north_hallway_B, 'south')

    #Constructing interior cafeteria connections (connecting the central 4 squares of the map).
    Room.connect_rooms(cafeteria_1A, 'east', cafeteria_1B, 'west')
    Room.connect_rooms(cafeteria_1A, 'south', cafeteria_2A, 'north')
    Room.connect_rooms(cafeteria_2A, 'east', cafeteria_2B, 'west')

    i = Item("Rock", "This is just a rock.")
    for room in Room.rooms:
        room.searchable_items.append(i)
        room.add_container_with_searchable('Chest', 'A large chest, possibly containing an item.')



    north_hallway_A.add_searchable_item(i)
    player.location = north_hallway_A

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
    if player.location.has_containers():
        print("This room contains the following containers:")
        for i in player.location.containers:
            print(i.name)
    print("You can go in the following directions:")
    for e in player.location.exit_names():
        print(e)
    print()

def show_help():
    clear()
    print("go <direction> -- moves you in the given direction")
    print("inventory -- opens your inventory")
    print("pickup <item> -- picks up the item")
    print("drop <item> -- drops the item")
    print("me -- prints the players current status")
    print("search -- searches a given room for items, different rooms can provide different items.")
    print("wait -- causes time to pass")
    print("open <container> -- opens a container in a room")
    print("hide -- allows you to hide in a room (if hiding spots are available) in order to escape the monster")
    print("inspect <location> <entity> -- allows you to inspect an item or container. the 'location' argument can take the letters i,c, and r. i will inspect an item in your inventory with the passed in entity name, c will look for a container in the room you are in, and r will get the description of an item in your room")
    print("quit -- quits the game")

    print()
    input("Press enter to continue...")


if __name__ == "__main__":
    create_world()
    playing = True
    print("Welcome to TBD! \n In this game you have to explore a decrepit school, hunting down three keys in order to escape. \n Be careful though, a terrifying monster is hunting you down! \n Type 'more' to get a further explanation on the features, otherwise press enter to begin the game!")
    if input('More info/continue: ').lower() == 'more':
        print("The monster is constantly roaming the school, entering and exiting rooms at random.\n If it sees you however, the chase will begin! \n Don't let yourself get caught, otherwise it's game over. \n While the monster is chasing you, you will be able to \'hide\' so that the monster won't be able to find you. \n There are also numerous items hidden around the map that can help you on your escape, keep an eye out! \n")
        input('Now, press enter to begin the game.')
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
                case "open":
                    target_name = command[5:]
                    print(target_name)
                    target = player.location.get_container_by_name(target_name.lower())
                    if target != False:
                        if target.needs_key_item == False:
                            player.open(target)
                        else:
                            ''
                    else:
                        print("No such container.")
                        command_success = False

                case "inventory":
                    player.show_inventory()
                case "help":
                    show_help()
                case "quit":
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
                case "search":
                    check = random.random()
                    if len(player.location.searchable_items)>0:
                        if check < player.search_chance:
                            item_num = random.randint(0, len(player.location.searchable_items)-1)
                            player.location.items.append(player.location.searchable_items[item_num])
                            print(f"You succesfully find {player.location.searchable_items[item_num].name} hidden in the room!")
                            del player.location.searchable_items[item_num]
                        else:
                            print('You failed to find anything here, although you feel like you might if you keep searching...')
                    else:
                        print('You failed to find anything here. There probably isn\'t anything left for you to find.')
                        time_passes = True
                case "wait":
                    print('You wait around for a little while.')
                    time_passes = True
                case "hide":
                    if player.location.has_hiding_spots == True:
                        print("You quietly slip into a hiding spot, attempting to avoid the monsters gaze.")
                        player.is_hidden = True
                        time_passes = True
                    else:
                        print("This room has no available hiding spots!")
                        command_success = False
                case "inspect":
                    if len(command_words) == 3:
                        target = command_words[2]
                        print(target)
                        in_list = False
                        match command_words[1]:
                            case "i":
                                for i in player.items:
                                    if i.name == target:
                                        i.describe()
                                        in_list = True
                                if not in_list:
                                    print(f'{target} is not in your inventory.')
                            case "c":
                                for i in player.location.containers:
                                    if i.name.lower() == target.lower():
                                        i.describe()
                                        in_list = True
                                if not in_list:
                                    print(f'{target} is not a container in this room.')
                            case "r":
                                ''
                            case other:
                                print('Not a valid argument for the inspect command')
                                command_success = False
                    else:
                        print('Wrong number of arguments for inspect command!')
                        command_success = False

                case other:
                    print("Not a valid command")
                    command_success = False
        if time_passes == True:
            updater.update_all()
            player.is_hidden = False





