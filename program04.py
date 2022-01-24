__author__ = 'Ella Seaman'
# 02/14/2021

def enterItems():
    items = []
    inputItems = True
    while inputItems:
        item = input("Enter item (press Enter to quit): ")
        items.append(item)
        if item == "":
            inputItems = False
    items.reverse()
    for item in items:
        print(item, sep="\n")

enterItems()