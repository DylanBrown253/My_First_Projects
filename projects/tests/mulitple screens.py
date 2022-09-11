import tkinter as tk 
def fnc1to2():
    print("1 to 2")
    frame1.pack_forget()
    frame2.pack()
def fnc1to3():
    print("1 to 3")
    frame1.pack_forget()
    frame3.pack()
def fnc2to3():
    print("2 to 3")
    frame2.pack_forget()
    frame3.pack()

def fnc3to1():
    print("3 to 1")
    frame3.pack_forget()
    frame1.pack()
root = tk.Tk() 

frame1 = tk.Frame(root, bg = "red")
frame2 = tk.Frame(root, bg = "blue")
frame3 = tk.Frame(root, bg = "green")

lab1f1 = tk.Label(frame1, text = "Label 1 in fram1")
lab1f2 = tk.Label(frame2, text = "Label 2 in fram2")
lab1f3 = tk.Label(frame3, text = "Label 3 in fram3")

btn1to3 = tk.Button(frame1, text = "1 to 3", command = fnc1to3)
btn1to2 = tk.Button(frame1, text = "1 to 2", command = fnc1to2)

btn2to3 = tk.Button(frame2, text=  "2 to 3", command = fnc2to3)

btn3to1 = tk.Button(frame3, text=  "3 to 1", command=fnc3to1)

#frame 1
lab1f1.pack()
btn1to3.pack()
btn1to2.pack()

#frame 2
lab1f2.pack()
username = tk.Entry(frame2, width=50, borderwidth= 4)
username.pack()
btn2to3.pack()

#frame 3
lab1f3.pack()
created_email = tk.Entry(frame3, width=50, borderwidth= 4)
created_email.pack()
created_password = tk.Entry(frame3, width=50, borderwidth= 4)
created_password.pack()
btn3to1.pack()


frame1.pack()
root.mainloop()
