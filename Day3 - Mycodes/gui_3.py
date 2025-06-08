import tkinter

root = tkinter.Tk()

entry = tkinter.Entry(root)
entry.pack()

def print_input(event):
    user_in=entry.get()
    print(user_in)

root.bind("<Return>", print_input)
root.bind("<space>", print_input)
root.mainloop()