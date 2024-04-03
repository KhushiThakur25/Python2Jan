from tkinter import*
window = Tk()
window.geometry('300x400')
window.title('Calculator')

expression = StringVar()

textBox = Entry(window, text = expression,font = (14), width=20,justify='right')
textBox.grid(row=0,columnspan=4,padx=10,pady=10, ipadx=10,ipady=10)
buttons = [
    ['c','<-','%','='],
     ['7','8','9','*'],
      ['4','5','6','/'],
       ['1','2','3','-'],
        ['.','0','e','+'],
]
def calc(event):
    # print(event.widget.cget('text'))
    value = event.widget.cget('text')
    expression = textBox.get()
    if value == '=':
        result = eval(expression)
        textBox.delete(0,END)
        textBox.insert(0,result)
    elif value == 'c':
         textBox.delete(0,END)
    elif value == '<-':
        textBox.delete(len(expression)-1)
    elif value == 'e':
        textBox.insert(END, str(2.718))
    else:
        textBox.insert(len(expression),value)
    


for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn = Button(window,text=buttons[i][j],font=('Arial',16),width=3)
        btn.grid(row=i+1,column=j,ipadx=5,ipady=5,pady=5)
        btn.bind('<Button-1>',calc)

window.mainloop()