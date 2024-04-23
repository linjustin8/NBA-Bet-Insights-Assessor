# results.py
from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from headshot import Headshots


class Results:
    def __init__(self, player, points, overUnder, algorithm, exTime, pointList):
        self.player = player
        self.points = points
        self.overUnder = overUnder
        self.algorithm = algorithm
        self.pointList = pointList
        self.exTime = exTime
        self.exTime *= 1000000
        self.exTime = round(self.exTime, 3)
        self.exTime = str(self.exTime)
        
    def getPercentage(self):
        pass
    
    def handleVisualizer(self, page, firstname, lastname):
        graph = Toplevel(page)
        graph.title("Data Visualizer")
        graph.geometry("510x510")

        imageFile = Image.open(f"assets/{firstname} {lastname}_graph.png")
        tkImage = ImageTk.PhotoImage(imageFile)
        
        playerData = CTkLabel(graph, image=tkImage, text="")
        playerData.image = tkImage # keeping a reference of the image
        playerData.grid(row=3, column=0)
        
        graph.columnconfigure(0, weight=1)
        graph.rowconfigure(0, weight=1)
        graph.grab_set()
        graph.transient(page)
    
    def split_name(self):
        split = self.player.strip().split()
        firstname = split[0]
        lastname = split[-1] if len(split)>1 else "" # ensures the element accessed is actually the last name
        return firstname, lastname
    
    def displayResults(self, inputPage):
        resultsPage = Toplevel(inputPage)
        resultsPage.title("Goat Gambler")
        resultsPage.geometry("800x1200")
        
        mainframe = Frame(resultsPage, width=790, height=990, highlightbackground="#6B6B6B", highlightthickness=8)
        mainframe.grid(row=0, column=0, sticky="nswe")
        resultsPage.columnconfigure(0, weight=1)
        resultsPage.rowconfigure(0, weight=1)
        
        # player title label
        title = CTkLabel(mainframe, text="PLAYER", font=("Lucida Console", 42, "bold", "underline"), text_color="#A0A0A0")
        title.grid(row=0, column=0, sticky="s", padx=10, pady=10)
        
        # player name label
        player = CTkLabel(mainframe, text=self.player.title(), font=("Lucida Console", 42, "bold"), text_color="black",
                          justify="center")
        player.grid(row=1, column=0, sticky="n")
              
        # Execution time label
        mu = "\u03BC"
        timeText = CTkLabel(mainframe, text="Exec. Time:", font=("Lucida Console", 32, "bold"), text_color="black")
        timeText.grid(row=7, column=0, sticky="nw", padx=20)
        timeOutput = CTkLabel(mainframe, text=f"{self.exTime}{mu}s", font=("Lucida Console", 32, "bold"), text_color="black")
        timeOutput.grid(row=7, column=0, sticky="ne", padx=20)
        
        # over/under input label
        ouText = CTkLabel(mainframe, text="OVER/UNDER(pts):", font=("Lucida Console", 32, "bold"), text_color="black")
        ouText.grid(row=8, column=0, sticky="w", padx=20)
        ouInput = CTkLabel(mainframe, text=self.points, font=("Lucida Console", 32, "bold"), text_color="black")
        ouInput.grid(row=8, column=0, sticky="e", padx=20)
    
        # playerImage
        firstname, lastname = self.split_name()
        imageFile = Image.open(f"../assets/{firstname}_{lastname}.png")
        imageFile = imageFile.resize((624, 456), Image.LANCZOS)
        tkImage = ImageTk.PhotoImage(imageFile)
        
        playerHeadshot = CTkLabel(mainframe, image=tkImage, text="")
        playerHeadshot.image = tkImage # keeping a reference of the image
        playerHeadshot.grid(row=3, column=0)
        
        # odds(percentage) label
        percentText = CTkLabel(mainframe, text="ODDS:", font=("Lucida Console", 32, "bold"), text_color="black")
        percentText.grid(row=9, column=0, sticky="sw", padx=20)
        percentOutput = CTkLabel(mainframe, text="33.91%", font=("Lucida Console", 32, "bold"), text_color="black")
        percentOutput.grid(row=9, column=0, sticky="se", padx=20)
        
        # open visualizer button
        openVisualizer = CTkButton(mainframe, fg_color="#A0A0A0", text="OPEN DATA VISUALIZER", hover_color="#4C4C4C",
                         font=("Lucida Console", 32, "bold"),corner_radius=25, height=50, width=400,
                         command=self.handleVisualizer(resultsPage, firstname, lastname), text_color="#282828")
        openVisualizer.grid(row=13, column=0, padx=10)
        
        
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure((0,1,2,4,5,6,7,8,9,10,11,12,13,14,15), weight=1)
        
        resultsPage.grab_set()
        resultsPage.transient(inputPage)