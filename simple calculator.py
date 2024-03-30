from tkinter import *

root=Tk()
root.title("Simple Calculator")

label1=Label(root,text="""
█▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄\n""",fg="purple",height=5)
label1.grid(row=0,columnspan=5)

result =StringVar()
#StringVar variable type is specifically designed to hold strings and is particularly useful for synchronizing the value of a widget

entry =Entry(root, textvariable=result, font=('Calibri', 13), width=40, borderwidth=3)
entry.grid(row=1, column=0, columnspan=6)

def calculate():
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")

buttons = ['7', '8', '9', '/','4', '5', '6', '*','1', '2', '3', '-','0', '.', '=', '+']
Label(root,text='').grid(row=2)
row = 3
col = 0

for b in buttons:
    Button(root, text=b,font=('Calibri', 14), width=11, fg='#C22381', command=lambda button=b: entry.insert(END, button)).grid(row=row, column=col)
    #lambda allows you to define a simple, anonymous function inline without explicitly naming it
    col += 1
    if col > 3:
        col = 0
        row += 1
Button(root, text='C', font=('Calibri', 14), width=11, fg='red',command=lambda:entry.delete(0,END)).grid(row=7, column=0, columnspan=2)
Button(root, text='=', font=('Calibri', 16), width=11, fg='green',command=calculate).grid(row=7, column=2, columnspan=2)

root.mainloop()