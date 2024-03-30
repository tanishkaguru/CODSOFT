from tkinter import *
root=Tk()
root.title("To-do list")

label1=Label(root,text="""\n
 ████████╗░█████╗░░░░░░░██████╗░░█████╗░
 ╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██╔══██╗
 ░░░██║░░░██║░░██║█████╗██║░░██║██║░░██║
 ░░░██║░░░██║░░██║╚════╝██║░░██║██║░░██║
 ░░░██║░░░╚█████╔╝░░░░░░██████╔╝╚█████╔╝
 ░░░╚═╝░░░░╚════╝░░░░░░░╚═════╝░░╚════╝░  \n""",fg="#9B2FA0",height=5)
label1.grid(row=0,columnspan=2)

def addtask():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)

def deletetask():
    try:
        taskindex = listbox.curselection()[0]
        listbox.delete(taskindex)
    except IndexError:
        pass

Label(root,text='').grid(row=1)
entry=Entry(root, width=40,fg='#B8287F',font=('Calibri',14))
entry.grid(row=2, column=0)

add_button = Button(root, text="Add Task", width=10, fg='#B541BA',font=('Calibri',14),command=addtask).grid(row=2, column=1, padx=5, pady=5)

Label(root,text='').grid(row=3)
listbox = Listbox(root, width=50,fg='#B8287F',font=('Calibri Bold',15))
listbox.grid(row=4, column=0, columnspan=2, padx=8, pady=10)

deletebutton = Button(root, text="Delete Task", width=10, fg='#B541BA',font=('Calibri',14), command=deletetask)
deletebutton.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()