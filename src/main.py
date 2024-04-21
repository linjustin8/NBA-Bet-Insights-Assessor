#main.py
from tkinter import *
from tkinter import ttk
from customtkinter import *

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
    player.grid(row=2, column=0)  
    print(player.cget("text_color"))

    #input widget for point value
    pts = CTkTextbox(mainframe, fg_color="#A0A0A0", font=("Lucida Console", 25), corner_radius=25, height=40, width=400)
    pts.insert(1.0, "Pts Over/Under...")
    pts.grid(row=3, column=0)  
    pts.bind("<FocusIn>", lambda event, p=pts: ptsFocused(event, p))
    pts.bind("<FocusOut>", lambda event, p=pts: ptsUnfocused(event, p))
    player.bind("<Return>", lambda event, p=pts: handleEnter(event, p)) 
    pts.bind("<Return>", lambda event, p=pts: handleEnter(event, p)) 
    
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure((0,1,2,4,5), weight=1)


    root.mainloop()


#sets focus to pts textbox after hitting enter
def handleEnter(event, pts):
    pts.focus_set()
    return "break"

def ptsFocused(event, textbox):
    if textbox.get(1.0,"end-1c") == "Pts Over/Under...":
        textbox.delete(1.0,"end-1c")
        textbox.configure(fg_color="#6B6B6B")
        textbox.configure(text_color="#FFFFFF")

def ptsUnfocused(event, textbox):
    if textbox.get(1.0,"end-1c") == "":
       textbox.insert(1.0, "Pts Over/Under...")
       textbox.configure(fg_color="#A0A0A0")
       textbox.configure(text_color="#DCE4EE")
       
def playerFocused(event, textbox):
    if textbox.get(1.0,"end-1c") == "Player Name...":
        textbox.delete(1.0,"end-1c") 
        textbox.configure(fg_color="#6B6B6B")
        textbox.configure(text_color="#FFFFFF")

def playerUnfocused(event, textbox):
    if textbox.get(1.0,"end-1c") == "":
       textbox.insert(1.0, "Player Name...")
       textbox.configure(fg_color="#A0A0A0")
       textbox.configure(text_color="#DCE4EE")



if __name__ == "__main__":
    main()