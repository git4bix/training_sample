"""
f_num = int(input("Please input the number: "))
s_num = int(input("Please input the number: "))

print(f_num > s_num)
print(f_num < s_num)

"""
"""
f_num = int(input("min input the number: "))
s_num = int(input("max input the number: "))
t_num = int(input("middle input the number: "))

print(f_num > t_num > s_num)
print(f_num < t_num < s_num)
print(s_num >= t_num >= f_num)

"""
"""
rpass = "pass"
rpass2 = "Pass"
inpass = input("please enter the correct password: ")

if inpass == rpass or inpass == rpass2 :
    print("access granted: ")
else:
    print("access denied")

print("\nend")
"""

inpass = input("please enter green, yellow and red:  ")

if inpass == "green":
    print("green means go")
elif inpass == "yellow":
    print("yellow means slow")
elif inpass == "red":
    print("red means stop")
else:
    print("malfunctions")
print("\nend")