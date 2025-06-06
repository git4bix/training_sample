num1 = 0
prog_stop = False
while not prog_stop:
    pili = input("provide command: ")
    if pili == "add":
        num1 += 1
            print(num1)
        elif pili == "minus":
            if num1 == 0:
                print("number is already zero")
            else:
                num1 -= 1
                print(num1)
        elif pili =="exit" :
            prog_stop = True