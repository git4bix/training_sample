import tkinter
import json

root = tkinter.Tk()
root.title("My Form")
root.geometry("400x400")

label1 = tkinter.Label(root, text="Name")
label1.grid(row=1, column=0, padx=10, pady=10)

label1 = tkinter.Label(root, text="Age")
label1.grid(row=2, column=0, padx=10, pady=10)

entry1 = tkinter.Entry(root)
entry1.grid(row=1, column=1, padx=10, pady=10)

entry2 = tkinter.Entry(root)
entry2.grid(row=2, column=1, padx=10, pady=10)

label3 = tkinter.Label(root, text="Preferred Theme")
label3.grid(row=3, column=0, padx=0, pady=0)

radio_var = tkinter.StringVar(value="Option A")
radio1 = tkinter.Radiobutton(root, text="Light", variable=radio_var, value="Option A")
radio2 = tkinter.Radiobutton(root, text="Dark",  variable=radio_var, value="Option B")
radio1.grid(row=3, column=1, padx=0, pady=0)
radio2.grid(row=3, column=2, padx=0, pady=0)

label4 = tkinter.Label(root, text="Subscribe to new letter")
label4.grid(row=4, column=0, padx=0, pady=0)
check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(root,text="Enable", variable=check_value)
checkbox.grid(row=4, column=1, padx=0, pady=0)

label5 = tkinter.Label(root, text="Rate Us")
label5.grid(row=5, column=0, padx=0, pady=0)

slider_value = tkinter.IntVar(value=0)
slider = tkinter.Scale(root, from_=0, to=100, orient="horizontal", variable=slider_value)
slider.grid(row=5, column=1, padx=0, pady=0)


def sub():
    user={"name":entry1.get(),"age":entry2.get(),"theme":radio_var.get() ,"subscribe": check_value.get(), "Ratings":slider_value.get()}
    #with open('people.json', 'w') as file:
        #json.dump(user, file, indent=4)

    #with open("test.txt", "w") as file:
        #file.write(user)



button1 = tkinter.Button(root, text="Submit", command=sub)
button1.grid(row=7, column=0, padx=0, pady=0)




root.mainloop()