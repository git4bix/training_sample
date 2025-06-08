import tkinter

def print_left(event):
    print("left pressed")

root = tkinter.Tk()

entry = tkinter.Entry(root)
entry.pack()

root.bind("<Left>", print_left)

root.mainloop()