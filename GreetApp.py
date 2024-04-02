from tkinter import*

window = Tk()
window.title('MyFirst App')

window.geometry('400x400')

def changeText():
    text = textBox.get()
    label_2.configure(text='Hello : ' + text)

label = Label(window, text="Enter your name:")
# label.grid(column=0,row=0)
label.place(x = 10,y = 10)

textBox = Entry(window, width=20, font=('Arial',15,'bold'))
# textBox.grid(column=1,row=0)
textBox.place(x = 10,y = 70)

label_2 = Label(window,text="", font=('Arial',20,'bold'))
# label_2.grid(column=0,row=2)
label_2.place(x = 10,y = 140)

btn = Button(window, text="Click Here" , fg='red',command=changeText)
# btn.grid(column=1,row=1)
btn.place(x = 250,y = 70,width=100 , height=30)

window.mainloop()
