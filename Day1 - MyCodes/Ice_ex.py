"""
con = 0
con +=1
con -=1
print(con)
"""
"""
samp = "ice"
samp2 = "baby"

print((samp+" ")*3, samp2)
"""
"""
mess1 = "your name is {}"
mess2 = "favorite number is {}"
mess3 = "favorite color is {}"

nam1 = input("name: ")
fav2 = int(input("number: "))
fav3 = input("color: ")

print(mess1.format(nam1))
print(mess2.format(fav2))
print(mess3.format(fav3))

"""

"""
mess1 = "your name is {}"
mess2 = "favorite number is {}"
mess3 = "favorite color is {}"

"""

nam1 = int(input("Please input the price for balot: "))
nam1_2 = int(input("how many items for the balot: "))
nam2 = int(input("Please input the price tinapay: "))
nam2_2 = int(input("how many items for the tinapay: "))
nam3 = int(input("Please input the price for itlog: "))
nam3_2 = int(input("how many items for the itlog: "))


tot_balot = nam1 * nam1_2
tot_tin = nam2 * nam2_2
tot_it = nam3 * nam3_2
tot_all = tot_it + tot_balot + tot_tin

print("\n without f format \n\n")

print("the total price for balot is: ", tot_balot)
print("the total price for tinapay is: ", tot_tin)
print("the total price for itlog is: ", tot_it)
print("the total price for all is: ", tot_all)

print("\n with f format \n\n")

print(f"The total price for balot is: {tot_balot} \nthe tinapay is: {tot_tin} \nthe itlog is: {tot_it} \nthe total price for your items: {tot_all}")