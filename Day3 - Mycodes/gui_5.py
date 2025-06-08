import tkinter

root = tkinter.Tk()

user_in = tkinter.StringVar(root, value="Enter the text")

next_label = tkinter.Label(root, textvariable=user_in)
next_label.pack()

entry = tkinter.Entry(root)
entry.pack()

def display(event):
    user_in.set(entry.get())
root.bind("<Return>", display)
root.mainloop()