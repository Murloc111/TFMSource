# coding: utf-8
import time

class Flyspeed:
    def __init__(self):
        self.mg = Minigames

        self.cats = [7, 17]

        self.players = {}

    def load(self):
        pass

    def event_mouseduck(self, player):
        pass

    def event_createroom(self, room):
        pass

    def event_newround(self, player):
        self.players[player.playerCode].mordido = False

    def event_enterroom(self, player):
        self.players[player.playerCode] = Player(player.username)
        player.enableKey(32)
        player.sendMessage("<VP>Welcome to <J>#flyspeed")
        player.sendMessage("<VP>For more information about this room press <T>TAB")
        player.enableKey(9)         
        player.enableKey(37)
        player.enableKey(38)
        player.enableKey(39)        
        
    def event_leaveroom(self, player):
        del self.players[player.playerCode]

    def event_die(self, player):
        pass

    def event_getcheese(self, player):
        pass
        
    def event_keypress(self, player, key):
        if key == 37:
                player.movePlayer(player.username, 0, 0, True, -50, 0, True)
        elif key == 38:
                player.movePlayer(player.username, 0, 0, True, 0, -20, True)
        elif key == 39:
                player.movePlayer(player.username, 0, 0, True, +50, 0, True)
        elif key == 9:
                player.sendMessage("<VP>In the room <J>#flyspeed <VP>you can move faster, press key <T>LEFT <VP>and <T>RIGHT<VP>. Also you can fly, press key <T>UP<VP>.")

class Player:
    def __init__(self, name):
        self.name = name
        self.ballons = 10
        self.nextshot = 0
        self.sx = 1
        self.sy = 1
        self.btpoints = 0
        self.mordido = False        

class Minigames:
    def initMinigame(self, name, room):
        f = False
        if name.startswith("flyspeed"):
            room.minigame = Flyspeed()
            f = True            
        return f