import tkinter
root = tkinter.Tk()
root.title("Sa akin ka")
root.geometry("1000x600")

label = tkinter.Label(root,
                      text="hello",
                      font=("Arial black", 40, "bold"),
                      fg="red",
                      bg="yellow",
                      width=1,
                      height=1,
                      padx=1,
                      pady=1
                      )
label.pack(side="left")

next_label = tkinter.Label(root, text="world")
next_label.pack()

message = """
 
marami kaming ginagaw

"""

next_label2 = tkinter.Label(root, text=message)
next_label2.pack(side="right")

root.mainloop()