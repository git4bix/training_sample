"""with open("test.txt", "w") as file:
    file.write("mukamo")"""

att =[]

with open("test.txt", "w") as file:
    file.write(" ")

att_num = int(input("how many students: "))

for attendance in range(att_num):
    attendance = (input("pleaes put your name: "))
    #att.strip()
    with open("test.txt", "a") as file:
        file.writelines(f"\n{attendance}")

with open("test.txt", "r") as file:
    file_contents = file.read()

print(file_contents)