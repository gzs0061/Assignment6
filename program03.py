__author__ = 'Ella Seaman'
# 02/14/2021

def enterNames():
    names = [item for item in input("Enter your name : ").split()]
    names.reverse()
    print(names)

enterNames()