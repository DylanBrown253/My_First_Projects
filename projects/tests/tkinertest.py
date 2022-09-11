import tkinter 
from tkinter import *
def click():
    print("Hello!")
window = Tk()
button = Button(window, text = 'Login' )
button.config(command=click) #performs call back of function
button.config(font=('Ink Free', 50, 'bold'))
button.config(bg='#000000')
button.config(fg='#327fc7')
button.config(activebackground='#333030')
button.config(activeforeground='#327fc7')
button.pack()
button2 = Button(window, text = 'Create Account')
button2.config(command=click) #performs call back of function
button2.config(font=('Ink Free', 25, 'bold'))
button2.config(bg='#000000')
button2.config(fg='#327fc7')
button2.config(activebackground='#333030')
button2.config(activeforeground='#327fc7')
button2.pack()
window.mainloop()
