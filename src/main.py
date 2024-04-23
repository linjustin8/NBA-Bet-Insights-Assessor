# main.py
from tkinter import *
from customtkinter import *
from data import *
from headshot import *
from results import Results
from mergesort import mergesort_alg
from quicksort import quicksort_alg

"""
input the following into terminal before running program:
    virtualenv venv
    venv/Scripts/activate
    pip install -r requirements.txt
    
to run:
    py src/main.py
"""


# Global Variables
playerName = ""
points = -1
overUnder = ""
sortingAlgorithm = ""
tStamp=0.00
pointList = []


def main():
    root = CTk()
    root.title("Goat Gambler")
    root.geometry("600x800")

    # creates the content frame of the gui
    mainframe = Frame(root, width=590, height=790, highlightbackground="#6B6B6B", highlightthickness=8)
    mainframe.grid(row=0, column=0, sticky="nswe")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # title widget
    title1 = Label(mainframe, text="Player", font=("Lucida Console", 48))
    title1.grid(row=0, column=0, sticky="s")
    title2 = Label(mainframe, text="Prediction", font=("Lucida Console", 48))
    title2.grid(row=1, column=0, sticky="n")

    # input widget for player
    player = CTkTextbox(mainframe, fg_color="#A0A0A0", font=("Lucida Console", 25), corner_radius=25, height=40, width=400)
    player.insert(1.0, "Player Name...")
    player.bind("<FocusIn>", lambda event, p=player: playerFocused(event, p))
    player.bind("<FocusOut>", lambda event, p=player: playerUnfocused(event, p))
    player.grid(row=4, column=0)  

    # input widget for point value
    pts = CTkTextbox(mainframe, fg_color="#A0A0A0", font=("Lucida Console", 25), corner_radius=25, height=40, width=400)
    pts.insert(1.0, "Pts Over/Under...")
    pts.grid(row=5, column=0)  
    pts.bind("<FocusIn>", lambda event, p=pts: ptsFocused(event, p))
    pts.bind("<FocusOut>", lambda event, p=pts: ptsUnfocused(event, p))
    player.bind("<Return>", lambda event, p=pts: handleEnter(event, p)) 
    player.bind("<Tab>", lambda event, p=pts: handleEnter(event, p)) 
    pts.bind("<Return>", lambda event, p=pts: handleEnter(event, p)) 
    pts.bind("<Tab>", lambda event, p=pts: handleEnter(event, p)) 
    
    # over under semented button
    overUnderSelect = CTkSegmentedButton(mainframe, values=["Over", "Under"], font=("Lucida Console", 25), height=60,
                                         corner_radius=25, fg_color="#C1C1C1", unselected_color= "#8E8E8E", selected_color="#282828",
                                         border_width=7.5, selected_hover_color="#5E5E5E", command=overUnderChoice)
    overUnderSelect.grid(row=6, column=0)
    
    # sorting algorithm segmented button
    algorithmSelect = CTkSegmentedButton(mainframe, values=["Quick Sort", "Merge Sort"], font=("Lucida Console", 25), height=60,
                                         corner_radius=25, fg_color="#C1C1C1", unselected_color= "#8E8E8E", selected_color="#282828",
                                         border_width=7.5, selected_hover_color="#5E5E5E", command=algorithmChoices)
    algorithmSelect.grid(row=7, column=0)    
    
    # finalize inputs button
    getResults = CTkButton(mainframe,fg_color="#A0A0A0", text="Finalize Selection", hover_color="#4C4C4C",
                         font=("Lucida Console", 25, "bold"),corner_radius=25, height=50, width=400,
                         command=lambda: handleClick(mainframe, player, pts), text_color="#282828")
    getResults.grid(row=9,column=0, sticky="n")

    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure((0,1,2,4,5,6,7,8,9,10), weight=1)


    root.mainloop()


#~~~~~~~~~~~~~~~ sets focus to pts textbox after hitting enter ~~~~~~~~~~~~~~~#
def handleEnter(event, pts):
    pts.focus_set()
    return "break"

def ptsFocused(event, textbox):
    if textbox.get(1.0,"end-1c") == "Pts Over/Under...":
        textbox.delete(1.0,"end-1c")
        textbox.configure(fg_color="#6B6B6B", text_color="#FFFFFF")

def ptsUnfocused(event, textbox):
    if textbox.get(1.0,"end-1c") == "":
       textbox.insert(1.0, "Pts Over/Under...")
       textbox.configure(fg_color="#A0A0A0", text_color="#DCE4EE")
       
def playerFocused(event, textbox):
    if textbox.get(1.0,"end-1c") == "Player Name...":
        textbox.delete(1.0,"end-1c") 
        textbox.configure(fg_color="#6B6B6B", text_color="#FFFFFF")

def playerUnfocused(event, textbox):
    if textbox.get(1.0,"end-1c") == "":
       textbox.insert(1.0, "Player Name...")
       textbox.configure(fg_color="#A0A0A0", text_color="#DCE4EE")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ select over/under ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def overUnderChoice(ou):
    global overUnder
    overUnder = ou


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ check inputs ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def checkInput(player, pts):
    df = dataframe_init()
    if (checkPts(df,pts) and checkName(df,player)):
        return True
    else :
        return False
        
def checkPts(df,points):
    if(points == ""):
        print("not work: pts!")
        return False 
    for char in points:
        if (not(ord(char) > 47 and ord(char) < 58) and (ord(char) != 46)):
            print("not work: pts!")
            return False    
    return True

def checkName(df,player):
    for char in player:
        if (not(ord(char) > 96 and ord(char) < 123) and (ord(char) != 32) 
            and (ord(char) != 45) and (ord(char) != 39) and (ord(char) != 46)):
            print("not work: name!")
            return False
    #also will need to implement a check to see if player exists in database
    if checker(df,player):
        return True
    else:#
        print("Player doesn't Exist!")
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ sort option ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def algorithmChoices(algorithm):
    global sortingAlgorithm
    sortingAlgorithm = algorithm


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ click button ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def handleClick(root, player, pts):
    playerName = player.get(1.0, "end-1c").lower()
    points = pts.get(1.0, "end-1c")
    if(not(checkInput(playerName,points))):
        print("FAILED")
        errorWindow(root)
        return
    
    #sets points to int value if checks clear
    points = float(points)
    print(sortingAlgorithm)

    print(overUnder)
    finderrr = Headshots(playerName,points)
    finderrr.downloadImage()
    another = finderrr.get_dataf()

    list_o_points = list_o_point_create(another, playerName)

    if (sortingAlgorithm == "Merge Sort"):
        tStamp = mergesort_alg(list_o_points)
    if (sortingAlgorithm == "Quick Sort"):
        tStamp = quicksort_alg(list_o_points)

    #convert tStamp value to string later with nano,micro,pico etc
    results = Results(playerName, points, overUnder, sortingAlgorithm, tStamp, pointList)
    results.displayResults(root)
    

def errorWindow(root):
    error = Toplevel(root)
    error.title("Error Occurred")
    error.geometry("400x400")
    
    mainframe = Frame(error, width=390, height=390, highlightbackground="black", 
                      highlightthickness=5, bg="#BCBCBC")
    mainframe.grid(row=0, column=0, sticky="nswe")
    error.columnconfigure(0, weight=1)
    error.rowconfigure(0, weight=1)
    
    errorMessage = CTkLabel(mainframe, text="ERROR", font=("Lucida Console", 48, "bold"), text_color="black")
    errorMessage.grid(row=1, column=0)
    
    errorMessage2 = CTkLabel(mainframe, text="Please Check Your Inputs", font=("Lucida Console", 20), text_color="#282828")
    errorMessage2.grid(row=2, column=0, sticky="n")
    
    close = CTkButton(mainframe, text="Close",fg_color="#A0A0A0", hover_color="#4C4C4C", 
                      text_color="#282828", font=("Lucida Console", 20), command=error.destroy)
    close.grid(row=4, column=0, sticky="n")
    
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure((0,1,2,3,5,6), weight=1)
    
    error.grab_set()
    error.transient(root)


if __name__ == "__main__":
    main()