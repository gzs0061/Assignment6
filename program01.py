__author__ = 'Ella Seaman'
# 02/14/2021

def votingAge ():
    age = int(input("How old are you? "))
    if age < 18:
        print("You are too young to vote.")
    else:
        print("You can vote.")

votingAge()