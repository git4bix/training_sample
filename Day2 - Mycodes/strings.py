"""
mes = "I am perfectly calm and everything is fine"
#print(len(mes))

uppcnt = 0
lowcnt = 0
spccnt = 0

for mes in mes:
    if len(mes) == mes.isupper():
        uppcnt += 1
    if len(mes) == mes.islower():
        lowcnt += 1
    if len(mes) == mes.isspace():
        spccnt += 1

print(uppcnt)
print(lowcnt)
print(spccnt)
"""
ema = input("please input your emai: ")  
if ema.endswith("@gmail.com") == True :
    print("valid email")
else:
    print("invalid email")
