from tkinter import *
from tkinter import messagebox
window = Tk()

window.title("SEMINAR ONLINE BUCKET BY RifqiAlderson")
window.geometry('600x300')

lbl = Label(window, text="Nama")
lbl.grid(column=0, row=0)
txt = Entry(window,width=38)
txt.grid(column=1, row=0)

def clicked():
   messagebox.showinfo('Enter', 'Selamat Atas Seminar Proposalnya '+ txt.get())
btn = Button(window, text='Enter', command=clicked)
btn.grid(column=2, row=0)

rad1 = Radiobutton(window,text='S.KP', value=1)
rad2 = Radiobutton(window,text='S.Proposal', value=2)
rad3 = Radiobutton(window,text='S.Hasil', value=3)
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)
rad1 = Radiobutton(window,text='First', value=1, command=clicked)


messagebox.showwarning('SEMINAR ONLINE BUCKET By RifqiAldersom', 'WELCOME TO THE SYSTEM')  #shows warning message
#messagebox.showerror('Message title', 'Message content')    #shows error message


window.mainloop()