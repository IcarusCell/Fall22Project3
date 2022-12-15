import random
import updater

class Demon_Spider:
    def __init__(self, room, player):
        room.add_monster(self)
        updater.register(self)
        self.name = 'Demon Spider'
        self.player = player
        self.room = room
        self.chasing_player = False
        self.monster_status= ''
    def update(self):
        self.monster_status = ''
        player_check = self.player_adj()
        first_seen = False
        if self.player.location == self.room and self.player.is_hidden == False:
            if self.player.wounded:
                input("The monster catches you. Its long spindley arms rend your flesh. Your consciousness fades to black.")
                self.player.alive = False
            else:
                input("The monster reaches out and slices you! You feel the sensation of warm, hot blood running down your leg.")
                self.player.wounded = True
        if player_check and not self.chasing_player and not self.player.is_hidden:
            self.monster_status = f"The monster has seen you! It will be hot on your trail! It is to the {player_check}"
            self.chasing_player = True
            first_seen = True
        elif self.chasing_player and not first_seen and not self.player.is_hidden:
            self.move_to(self.player.previous_location)
            player_check = self.player_adj()
            if player_check:
                self.monster_status = f"The monster follows you at a haunting pace, coming from the {player_check}"
            else:
                self.monster_status = "As you cower in fear, the monster slowly creeps into the room, sniffing loudly trying to find where you are."
        elif self.chasing_player and self.player.is_hidden and self.player_adj():
            self.move_to(self.player.location)
            self.monster_status = "The monster enters your room and sniffs around."
            self.chasing_player = False
        elif self.player.is_hidden and self.room == self.player.location:
                self.move_to(self.room.random_neighbor())
                self.chasing_player = False
                self.monster_status += f'\nThe monster moves along to the {self.player_adj()}, but it is still nearby. Be very careful...'

        else:

            if not self.chasing_player:
                self.move_to(self.room.random_neighbor())
                if self.player_adj():
                    self.monster_status = f'The monster has found you! It crept up on you from the {self.player_adj()}'
                    self.chasing_player = True
                elif self.player.location == self.room and self.player.is_hidden:
                    self.monster_status = 'The monster enters the the room with you, but it hasn\'t noticed you. Yet...'
            if self.player.is_hidden and self.player_adj():
                self.monster_status = f'The monster cannot see you right now but it is directly to the {self.player_adj()}'

    def move_to(self, room):
        self.room.remove_monster(self)
        self.room = room
        room.add_monster(self)
    def player_adj(self):
        for i in self.player.location.exits:
            if i[1] == self.room:
                return i[0]
        return False
class Monster:
    def __init__(self, name, health, room):
        self.name = name
        self.health = health
        self.room = room
        room.add_monster(self)
        updater.register(self)
    def update(self):
        if random.random() < .5:
            self.move_to(self.room.random_neighbor())
    def move_to(self, room):
        self.room.remove_monster(self)
        self.room = room
        room.add_monster(self)
    def die(self):
        self.room.remove_monster(self)
        updater.deregister(self)
