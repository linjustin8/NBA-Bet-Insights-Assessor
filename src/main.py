#main.py
from tkinter import *
from tkinter import ttk
from customtkinter import *

#pip install tkinter
#pip install requests
#pip install customtkinter


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
    player = CTkTextbox(mainframe, fg_color="#6B6B6B", font=("Lucida Console", 30), corner_radius=25, height=40, width=400)
    player.grid(row=2, column=0)  

    #input widget for point value
    pts = CTkTextbox(mainframe, fg_color="#6B6B6B", font=("Lucida Console", 30), corner_radius=25, height=40, width=400)
    pts.grid(row=3, column=0)  
    player.bind('<Return>', lambda event, p=pts: handleEnter(event, p)) 
    pts.bind('<Return>', lambda event, p=pts: handleEnter(event, p)) 
    
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure((0,1,2,4,5), weight=1)

    # playerEntry.rowconfigure(weight=1)

    # for child in mainframe.winfo_children(): 
    #     child.grid_configure(padx=30, pady=30)
    root.mainloop()


#sets focus to pts textbox after hitting enter
def handleEnter(event, pts):
    pts.focus_set()
    return "break"

if __name__ == "__main__":
    main()