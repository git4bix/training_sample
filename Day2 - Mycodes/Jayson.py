"""
fav_list = { "Number": 5,
             "color" : "vanta black",
             "Hobby": "motor"
             }

for bil, bi2 in fav_list.items():
    print(bil,bi2)
"""

"""
country_codes = {
"PH": "Philippines",
"US": "United States",
"SG": "Singapore",
}
code = input("Enter country code: ")

print(f"{code} -> {country_codes.get[code]}")
"""
"""
att = dict()

att_num = int(input("how many students: "))

for attendance in range(att_num):
    nam1 = input("please input your name: ")
    nam2 = input("please input the task: ")
    att[nam1] = [nam2]
 
 print(att)
"""
"""
#exam = []
for number in range(10):
    exam.append(number+1)
    print(exam)


exam1 = [number + 1 for number in range(10)]
print(exam1)
"""
"""

cant = []
num_cnt = int(input("how many to genarate: "))
#cnt = [number * number for number in range(num_cnt)]
#print(cnt)

for num_cnt in range(num_cnt):
    cant.append(num_cnt*num_cnt)

print(cant)
"""
"""
requests = {"Andrew": 10, "Peddy": 21, "Alex": 30}
banned = {"Alex"}
adults = [name for name, age in requests.items() if age >= 18]
print(adults)
allowed = [name for name in adults if name not in banned]
print(allowed)
"""
"""
coordinates = []
for x in range(10):
    for y in range(10):
        for z in range(10):
            coordinates.append((x, y, z))
print(coordinates)
"""

heroes = ['Knight', 'Archer', 'Mage', 'Cleric']
monsters = ['Slime', 'Orc', 'Chocobo', 'Dragon']
pacifist = ['Cleric','Chocobo']

pairing = [ (hero, monster)
                for hero in heroes
                for monster in monsters
]
print(pairing)

winner = []
for hero in heroes:
    for monster in monsters:
        for pacifis in pacifist:
            if len(hero) > len(monster):
                winner.append(hero)
            elif len(monster) > len(hero):
                winner.append(monster)
            elif len(hero) == pacifist:
                winner.append("draw")
            elif len(monster) == pacifist :
                winner.append("draw")
print(winner)


