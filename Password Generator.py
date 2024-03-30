from tkinter import *

root=Tk()
root.title("Password Generator")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

label1=Label(root,text="""
█▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
█▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄\n""",fg="#F7A2D4",height=5)
label1.grid(row=0,columnspan=2)

def generate():
    let=int(entry1.get())
    sym=int(entry2.get())
    num=int(entry3.get())
    pas=""
    for i in range(let):
        ind = random.randint(0, 51)
        pas += f"{letters[ind]}"
    for i in range(sym):
        ind = random.randint(0, 8)
        pas += f"{symbols[ind]}"
    for i in range(num):
        ind = random.randint(0, 9)
        pas += f"{numbers[ind]}"
    pas=list(pas)
    random.shuffle(pas)
    pas="".join(pas)
    result.set(pas)

Label(root,text='Enter the number of letters: ',fg='purple',font=('Calibri',14)).grid(row=1,column=0)
entry1 = Entry(root,fg='pink',font=('Calibri',13),width=10)
entry1.grid(row=1,column=1)

Label(root,text='Enter the number of symbols: ',fg='purple',font=('Calibri',14)).grid(row=2,column=0)
entry2 = Entry(root,fg='pink',font=('Calibri',13),width=10)
entry2.grid(row=2,column=1)

Label(root,text='Enter the number of numbers: ',fg='purple',font=('Calibri',14)).grid(row=3,column=0)
entry3 = Entry(root,fg='pink',font=('Calibri',13),width=10)
entry3.grid(row=3,column=1)

Label(root,text='').grid(row=4)
Button(root,text="GENERATE PASSWORD",font=('Calibri',13),fg='#4E1B5D',bg='#FADBEE',command=generate,width=30).grid(row=5,column=1)
Label(root,text='').grid(row=6)

result =StringVar()

Label(root,text='Your generated password is: ',fg='#4E1B5D',font=('Calibri',14)).grid(row=7,column=0)
e4=Entry(root,fg='#F00B96',textvariable=result, font=('Calibri',13),width=30)
e4.grid(row=7,column=1)
Label(root,text='').grid(row=8)

root.mainloop()