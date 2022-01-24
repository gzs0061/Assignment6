__author__ = 'Ella Seaman'
# 02/14/2021

def sale_price():
    sales = float(input("What is the sale price? "))

    if sales >= 200.00:
        discount = 0.10

    elif 200.00 > sales >= 100.00:
        discount = 0.05

    else:
        discount = 0.00

    discount_amount = sales * discount
    final_price = sales - discount_amount
    print("Sales:$", sales, "Discount Amount:$", discount_amount, "You pay:$", final_price)


sale_price()
