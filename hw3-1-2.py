# Author JRI 9/29/21

card1_value = input("enter value of your first card ")
card2_value = input("enter value of your second card ")

if int(card1_value) + int(card2_value) <= 21:
    print("safe")
else:
    print("bust")
