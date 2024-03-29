from tkinter import*

# 1.window
root = Tk()

root.title("Tkinter GUI")
root.geometry('400x400')
label_1 = Label(root, text="Hello Khushi..")
label_1.grid(row=0,column=0)
#widgets
label = Label(root, text="Hello world..")
label.grid(row=0,column=1)
#label.pack()
#label.place(x = 10,y=10)
# label.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()

