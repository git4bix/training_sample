import tkinter

root = tkinter.Tk()

entry = tkinter.Entry(root)
entry.pack()

def print_input(event):
    next_label = tkinter.Label(root, text=entry.get())
    next_label.pack()


root.bind("<Return>", print_input)

root.mainloop()