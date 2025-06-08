import tkinter

root = tkinter.Tk()
root.title("MY SAMPLE")


next_label = tkinter.Label(root, text="Please Enter Your Password", height=10, width=50)
next_label.pack()

entry = tkinter.Entry(root)
entry.pack()
pass_entry = tkinter.StringVar(root, value="")
pass_label = tkinter.Label(root, textvariable=pass_entry)
pass_label.pack()

def display(event=None):
    pass1="12345"
    if entry.get() == pass1:
        pass_entry.set(value="Password Correct")
    else:
        pass_entry.set(value="Password Incorrect")
root.bind("<Return>", display)
but = tkinter.Button(root, text="Submit", command=display)
but.pack()

root.mainloop()