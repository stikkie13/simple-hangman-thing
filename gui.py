from tkinter import *
from hangman import hangman
root = Tk()
root.title('Hangman: the game')
Hangman = hangman(input('choose the word: ',))
def placement(widget, height, width):
    return widget.place(in_ = frame, anchor=N, relx=width, rely=height)

def guessing(letter, index, mode):
    Hangman.check(guess.get())
    theWord.config(text=Hangman.ShowGuess())
    inputField.delete(0)
    Canvas.itemconfig(self=display, tagOrId="item-"+str(Hangman.score), state=NORMAL)
    if Hangman.points():
        inputField.config(state=DISABLED)

#widgets
frame = Frame(root)
frame.pack(expand=True,fill=BOTH)

#The visuals----------------
display = Canvas(frame, height= 250,width=250)
#stage 1
hill = display.create_oval(0,200,250,310, outline="black", fill="black", width=2, state=HIDDEN, tags="item-1")
pole = display.create_line(70,205,70,45, fill="black", width= 4, state=HIDDEN, tags="item-1")
#stage 2
support = display.create_line(70,70,90,50, fill="black", width= 2, state=HIDDEN, tags="item-2")
lat = display.create_line(70,50,155,50, fill="black", width= 3, state=HIDDEN, tags="item-2")
#stage 3
rope = display.create_line(125,50,125,80, fill="black", width=3, dash=(3,1), state=HIDDEN, tags="item-3")
head = display.create_oval(115,80,135,100, outline="black", width=2, state=HIDDEN, tags="item-3")
#stage 4
torso = display.create_line(125,100,125,150, fill="black", width=2, state=HIDDEN, tags="item-4")
#stage 5
armLeft = display.create_line(125,105,110,120, fill="black", width=2, state=HIDDEN, tags="item-5")
armright = display.create_line(125,105,140,120, fill="black", width=2, state=HIDDEN, tags="item-5")
#stage 6
legLeft = display.create_line(125,150,110,180, fill="black", width=2, state=HIDDEN, tags="item-6")
legright = display.create_line(125,150,140,180, fill="black", width=2, state=HIDDEN, tags="item-6")
failure = display.create_text(125,230, fill="white", state=HIDDEN, justify=CENTER, text="YOU LOSE", tags="item-6")
#---------------------------

guess = StringVar(root, value='')
guess.trace_add('write', guessing)

inputField = Entry(frame,width=1,textvariable=guess,justify=CENTER,bd=0,state=NORMAL)

theWord = Label(frame, text=Hangman.ShowGuess())

FlavourText = Label(frame, text="choose a letter:")

#placement of the widgets 0,0 to 1,1
placement(inputField, 0.9, 0.5)
placement(FlavourText, 0.83, 0.5)
placement(display, 0.15, 0.5)
placement(theWord, 0.13, 0.5)

#set the size of the window
root.geometry("400x400")
root.minsize(400,400)
root.maxsize(400,400)
#run the bitch
root.mainloop()
