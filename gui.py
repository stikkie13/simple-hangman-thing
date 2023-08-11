from tkinter import *
root = Tk()
root.title('Hangman: the game')

def placement(widget, height, width):
    return widget.place(in_ = frame, anchor=N, relx=width, rely=height)

def guessing(letter, index, mode):
    print(guess.get(), len(guess.get()), str(inputField.state))
    if len(guess.get()) >= 1:
        inputField.state = DISABLED

#widgets
frame = Frame(root)
frame.pack(expand=True,fill=BOTH)

#The visuals
display = Canvas(frame, height= 250,width=250)
#stage 1
hill = display.create_oval(0,200,250,310, outline="black", fill="black", width=2)
pole = display.create_line(70,205,70,45, fill="black", width= 4)
#stage 2
support = display.create_line(70,70,90,50, fill="black", width= 2)
lat = display.create_line(70,50,155,50, fill="black", width= 3)
#stage 3
rope = display.create_line(125,50,125,80, fill="black", width=3, dash=(3,1))
head = display.create_oval(115,80,135,100, outline="black", width=2)
#stage 4
torso = display.create_line(125,100,125,150, fill="black", width=2)
#stage 5
armLeft = display.create_line(125,105,110,120, fill="black", width=2)
armright = display.create_line(125,105,140,120, fill="black", width=2)
#stage 6
legLeft = display.create_line(125,150,110,180, fill="black", width=2)
legright = display.create_line(125,150,140,180, fill="black", width=2)

guess = StringVar(root, value='')
guess.trace_add('write', guessing)

inputField = Entry(frame,width=1,justify=CENTER,bd=0,state=NORMAL,readonlybackground="white",textvariable=guess)


FlavourText = Label(frame, text="choose a letter:")

#placement of the widgets 0,0 to 1,1
placement(inputField, 0.9, 0.5)
placement(FlavourText, 0.83, 0.5)
placement(display, 0.15, 0.5)

#set the size of the window
root.geometry("400x400")
root.minsize(400,400)
root.maxsize(400,400)



#run the bitch
root.mainloop()
