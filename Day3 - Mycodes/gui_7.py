import tkinter

root = tkinter.Tk()
root.title("MY SAMPLE")


count = tkinter.IntVar(root, value=0)
label = tkinter.Label(root, textvariable=count)
label.pack()

def increment():
    count.set(count.get() + 1)

def decrease():
    if count.get() <= 0:
        count.set(value=0)
    else:
        count.set(count.get() - 1)

button1 = tkinter.Button(root, text=" + ", command=increment)
button1.pack()

button2 = tkinter.Button(root, text=" - ", command=decrease)
button2.pack()

root.mainloop()