from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('tic tac toe')
#root.iconbitmap('')

#x starts so true
clicked =True
count = 0
#disable all buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

#check to see if someone won
def checkifwon():
    global winner
    winner = False

    if b1["text"]=="x" and b2["text"]=="x" and b3["text"]=="x":
        b1.config(bg="blue")
        b1.config(bg="blue")
        b1.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations x wins")
        disable_all_buttons()

    elif  b4["text"]=="x" and b5["text"]=="x" and b6["text"]=="x":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations x wins")
        disable_all_buttons()

    elif b7["text"]=="x" and b8["text"]=="x" and b9["text"]=="x":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations x wins")
        disable_all_buttons()
    
    elif b1["text"]=="x" and b4["text"]=="x" and b7["text"]=="x":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations x wins")
        disable_all_buttons()

    elif b2["text"]=="x" and b5["text"]=="x" and b8["text"]=="x":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations x wins")
        disable_all_buttons()

    elif b3["text"]=="x" and b6["text"]=="x" and b9["text"]=="x":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations x wins")
        disable_all_buttons()

    elif b1["text"]=="x" and b5["text"]=="x" and b9["text"]=="x":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations x wins")
        disable_all_buttons()
    
    elif b3["text"]=="x" and b5["text"]=="x" and b7["text"]=="x":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations x wins")
        disable_all_buttons()


# check for o
    elif b1["text"]=="o" and b2["text"]=="o" and b3["text"]=="o":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations o wins")
        disable_all_buttons()

    elif b4["text"]=="o" and b5["text"]=="o" and b6["text"]=="o":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations o wins")
        disable_all_buttons()

    elif b7["text"]=="o" and b8["text"]=="o" and b9["text"]=="o":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations o wins")
        disable_all_buttons()
    
    elif b1["text"]=="o" and b4["text"]=="o" and b7["text"]=="o":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations o wins")
        disable_all_buttons()

    elif b2["text"]=="o" and b5["text"]=="o" and b8["text"]=="o":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations o wins")
        disable_all_buttons()

    elif b3["text"]=="o" and b6["text"]=="o" and b9["text"]=="o":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations o wins")
        disable_all_buttons()

    elif b1["text"]=="o" and b5["text"]=="o" and b9["text"]=="o":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations o wins")
        disable_all_buttons()
    
    elif b3["text"]=="o" and b5["text"]=="o" and b7["text"]=="o":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        winner= True
        messagebox.showinfo("tic tac toe","congratulations o wins")
        disable_all_buttons()

    #check if tie
    if count == 9 and winner== False:
        messagebox.showinfo("tic tac toe","Hey it's a tie \n Sorry!No one wins.")
        disable_all_buttons()

#button clicked functions
def b_click(b):
    global clicked,count

    if b["text"] == " " and clicked ==True:
        b["text"]="x"
        clicked=False
        count+=1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"]="o"
        clicked=True
        count+=1
        checkifwon()
    else:
        messagebox.showerror("tic tac toe","hey! that box is already selected\n pick another box")

def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked,count
    clicked= True
    count=0
# build the buttons
    b1= Button(root,text=" ",font=("helvetica",20),height=4,width=6,bg="SystemButtonFace",command=lambda:b_click(b1))
    b2= Button(root,text=" ",font=("helvetica",20),height=4,width=6,bg="SystemButtonFace",command=lambda:b_click(b2))
    b3= Button(root,text=" ",font=("helvetica",20),height=4,width=6,bg="SystemButtonFace",command=lambda:b_click(b3))

    b4= Button(root,text=" ",font=("helvetica",20),height=4,width=6,bg="SystemButtonFace",command=lambda:b_click(b4))
    b5= Button(root,text=" ",font=("helvetica",20),height=4,width=6,bg="SystemButtonFace",command=lambda:b_click(b5))
    b6= Button(root,text=" ",font=("helvetica",20),height=4,width=6,bg="SystemButtonFace",command=lambda:b_click(b6))

    b7= Button(root,text=" ",font=("helvetica",20),height=4,width=6,bg="SystemButtonFace",command=lambda:b_click(b7))
    b8= Button(root,text=" ",font=("helvetica",20),height=4,width=6,bg="SystemButtonFace",command=lambda:b_click(b8))
    b9= Button(root,text=" ",font=("helvetica",20),height=4,width=6,bg="SystemButtonFace",command=lambda:b_click(b9))

    #grid the buttons to screen
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

#check menu
my_menu = Menu(root)
root.config(menu=my_menu)

#create options 
options_menu = Menu(my_menu, tearoff=FALSE)
my_menu.add_cascade(label="Options" , menu=options_menu)
options_menu.add_command(label="reset game", command=reset)
reset()
root.mainloop()