from tkinter import*

# 1.window
root = Tk()

root.title("Tkinter GUI")
root.geometry('400x400')
def changeText():
    label.configure(text='Bye from Khushi..')

label = Label(root, text="Hello from Khushi..")
label.grid()

btn = Button(root, text="Click Here" , fg="red" , command=changeText)
btn.grid(column=1,row=0)


# label_1 = Label(root, text="Hello Khushi..")
# label_1.grid(row=0,column=0)
# #widgets
# label = Label(root, text="Hello world..")
# label.grid(row=0,column=1)

# bt_1 = Button(root,text="Click here",background='red',fg = 'white')
# bt_1.pack(expand=True,fill=BOTH,side = LEFT)

# bt_2 = Button(root,text="Click here",background='green',fg = 'white')
# bt_2.pack(expand=True,fill=BOTH,side = LEFT)

# bt_3 = Button(root,text="Click here",background='blue',fg = 'white')
# bt_3.pack(expand=True,fill=BOTH,side = LEFT)

# bt_4 = Button(root,text="Click here",background='pink',fg = 'black')
# bt_4.pack(expand=True,fill=BOTH,side = LEFT)
#label.pack()
#label.place(x = 10,y=10)
# label.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()

