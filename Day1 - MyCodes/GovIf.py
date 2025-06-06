
"""
gov_id = input("please in put your goverment ID [Y/N]: ")
nbi_id = input("please in put your NBI ID [Y/N]: ")
reg_id = input("please in put your Registration ID ID [Y/N]: ")
"""
"""
if gov_id == "y" and nbi_id == "y" and reg_id == "y":
    print("processing finished: ")
else:
    print("incomplete ID's")
"""
"""
match gov_id:
    case gov_id == "y" && nbi_id == "y" && reg_id == "y":
        print("processing finished: ")
    case _:
    print("incomplete ID's")
print("\nthank you")

"""

num1 = int(input("please input number: "))

if num1 >= 0 and num1 <= 10:
    print("special number")
else:
    print("not a special numebr")