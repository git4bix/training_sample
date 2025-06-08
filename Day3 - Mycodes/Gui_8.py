import tkinter

root = tkinter.Tk()


root.title("MY SAMPLE")
check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
root,
text="Enable",
variable=check_value
)
checkbox.pack()
root.mainloop()

