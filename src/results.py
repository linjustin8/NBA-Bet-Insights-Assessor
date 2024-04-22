# results.py
from tkinter import *
from customtkinter import *
from headshot import Headshots

class Results:
    def __init__(self, player, points):
        self.player = player
        self.points = points
        
    def getPercentage(self):
        pass
        
    def displayResults(self, inputPage):
        resultsPage = Toplevel(inputPage)
        resultsPage.title("Goat Gambler")
        resultsPage.geometry("600x800")
        
        mainframe = Frame(resultsPage, width=590, height=790, highlightbackground="#6B6B6B", highlightthickness=8)
        mainframe.grid(row=0, column=0, sticky="nswe")
        resultsPage.columnconfigure(0, weight=1)
        resultsPage.rowconfigure(0, weight=1)
        
        # player title label
        title = CTkLabel(mainframe, text="PLAYER:", font=("Lucida Console", 48, "bold", "underlined"), text_color="black")
        title.grid(row=1, column=1)
        
        # player name label
        
        
        # over/under input label
        
        
        # odds(percentage) label
        
        
        # open visualizer button
        
        
        
        mainframe.columnconfigure(0,1,2, weight=1)
        mainframe.rowconfigure((0,1,2,4,5,6,7), weight=1)
        
        resultsPage.grab_set()
        resultsPage.transient(inputPage)