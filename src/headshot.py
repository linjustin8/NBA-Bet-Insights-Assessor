#headshot.py
import requests

class Headshots:
    def __init__(self, player):
        self.player = player
        self.playerID = self.getPlayerID(self.player)
        
    def getPlayerID(self, player):
        pass
    
    def downloadImage(self):
        pass