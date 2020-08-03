from tkinter import *
import tkinter as tk
import json
def saver():
    U1 = entry1.get()
    U2 = entry2.get()
    U3 = entry3.get()
    unm = "Username:" + U2 +"\n"
    pwd = "Password:" + U3 +"\n"
    web = "Website:" + U1 +"\n"
    file = open('file1.txt','a')
    file.write(web)
    file.write(unm)
    file.write(pwd)

def viewer():
    file = open("file1.txt","r")
    for each in file:
        print(each)
    
    
roots = Tk()
roots.title('Password Saver Tool')
roots.configure(background = 'azure')
roots.geometry('600x600')
roots.resizable(0,0)

label1=Label(roots,text='Website:')
label1.place(x=170,y=120)
entry1=Entry(background = 'linen')
entry1.place(x=250,y=120)
label2=Label(roots,text='Username:')
label2.place(x=170,y=170)
entry2=Entry(background = 'linen')
entry2.place(x=250,y=170)
label3=Label(roots,text='Password:')
label3.place(x=170,y=220)
entry3=Entry(background = 'linen',show="*")
entry3.place(x=250,y=220)


button1=Button(roots,text='Save',background='sky blue',activebackground = 'blue', command=saver)
button1.place(x=190,y=320)
button2=Button(roots,text='View',background='sky blue',activebackground = 'blue', command=viewer)
button2.place(x=300,y=320)

roots.mainloop()
