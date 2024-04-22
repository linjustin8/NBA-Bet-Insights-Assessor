#main.py
from tkinter import *
from customtkinter import *
from heap import *

"""
input the following into terminal before running program:
    virtualenv venv
    venv/Scripts/activate
    pip install -r requirements.txt
    
to run:
    py src/main.py
"""


def main():
    root = CTk()
    root.title("Goat Gambler")
    root.geometry("600x800")

    #creates the content frame of the gui
    mainframe = Frame(root, width=590, height=790, highlightbackground="#6B6B6B", highlightthickness=8)
    mainframe.grid(row=0, column=0, sticky="nswe")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    #title widget
    title1 = Label(mainframe, text="Player", font=("Lucida Console", 48))
    title1.grid(row=0, column=0, sticky="s")
    title2 = Label(mainframe, text="Prediction", font=("Lucida Console", 48))
    title2.grid(row=1, column=0, sticky="n")

    #input widget for player
    player = CTkTextbox(mainframe, fg_color="#A0A0A0", font=("Lucida Console", 25), corner_radius=25, height=40, width=400)
    player.insert(1.0, "Player Name...")
    player.bind("<FocusIn>", lambda event, p=player: playerFocused(event, p))
    player.bind("<FocusOut>", lambda event, p=player: playerUnfocused(event, p))
    player.grid(row=3, column=0)  
    print(player.cget("text_color"))

    #input widget for point value
    pts = CTkTextbox(mainframe, fg_color="#A0A0A0", font=("Lucida Console", 25), corner_radius=25, height=40, width=400)
    pts.insert(1.0, "Pts Over/Under...")
    pts.grid(row=4, column=0)  
    pts.bind("<FocusIn>", lambda event, p=pts: ptsFocused(event, p))
    pts.bind("<FocusOut>", lambda event, p=pts: ptsUnfocused(event, p))
    player.bind("<Return>", lambda event, p=pts: handleEnter(event, p)) 
    pts.bind("<Return>", lambda event, p=pts: handleEnter(event, p)) 
    
    #finalize inputs button
    getResults = CTkButton(mainframe,fg_color="#A0A0A0", text="Finalize Selection", hover_color="#383838",
                         font=("Lucida Console", 25),corner_radius=25, height=40, width=400,
                         command=lambda: checkInput(player.get(1.0, "end-1c"), pts.get(1.0, "end-1c")))
    getResults.grid(row=6,column=0, sticky="n")



    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure((0,1,2,4,5,6,7), weight=1)


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



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ check inputs ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def checkInput(player, pts):
    # df = dataframe_init()
    if (checkPts(pts) and checkName(player)):
        print("WORKING")
        
    else :
        print("FAILED")
        
def checkPts(points):
    for char in points:
        if (not(ord(char) > 47 and ord(char) < 58)):
            print("not work: pts!")
            return False    
    return True

def checkName(player):
    for char in player:
        if (not(ord(char) > 96 and ord(char) < 123) and (ord(char) != 32) 
            and (ord(char) != 45) and (ord(char) != 39)):
            print("not work: name!")
            return False
    #also will need to implement a check to see if player exists in database
    return True



if __name__ == "__main__":
    main()