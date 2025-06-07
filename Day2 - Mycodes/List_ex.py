"""
items =['msg1', 'msg2','msg3']

for items[0] in items[2]:
    print(items[1])
"""
"""
items =['a', 'b','c','d','e','f','g','h','i','i']
#for items in items:
items[0] = '*'
items[2] = '*'
items[4] = '*'

print(items)
"""
"""
items =('a', 'b','c','d','e','f','g','h','i','i')
print(items) 

"""
"""
stu_dat = [("mukamo",98),("4bix",60),("max",80)]

print(stu_dat[1][1])
"""
"""
stu1 = ['juan','maria','joe']
sco = [70,90,81]

print("Student score: \n")
for stu1, sco  in zip(stu1, sco):
    print(f"Record: {stu1} scored {sco} in the exam")
    if stu1 > stu1 and sco > sco:
        print(f"the highest student{stu1} with the score of {sco}")
"""
"""
stu1 = ['juan','maria','joe']
for index, stu1 in enumerate(stu1, start=1):
    print(f"Student: {index}. {stu1}")
"""
"""
stu1 = ['juan','maria','joe']
tsk1 = ['task1','task2','task3']

for i in stu1:
    for r in tsk1:
        print(f"{i} - {r}")
"""
"""
let = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(let[0:3])
print(let[7:12])
print(let[23:])
"""

"""

stu1 = ['juan','maria','joe']

while True:
    ask1 = input("please enter your name:\n")

    if ask1 in stu1:
        print("access granted!")
    else:
        print("access denied")
"""
"""
sco = [70,90,81,75,83,98,97]
print("the lowest score is", min(sco))
print("the highest score is", max(sco))
print("the average score is", round(sum(sco)/7,2))

"""
att = []
att_num = int(input("how many students: "))

for attendance in range(att_num):
    att.append(input("pleaes put your name: "))

for attendance in range(att_num):
    print(f"names of students attanding: {att[attendance]}")

sme = "jd"
print("the number of stundent that you the same name: ", att.count(sme))