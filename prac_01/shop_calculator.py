total_price = 0
number_of_item = int(input("Enter a number of iteams: "))

while number_of_item <= 0:
    print("Invalid number of iteams!")
    number_of_item = int(input("Please Enter a number of iteams: "))

for i in range(number_of_item):
    price = float(input("Enter a price of iteam: "))
    total_price += price

if total_price >= 100:
    total_price *=0.9

print(f"Total price for {number_of_item} items is ${total_price:.2f}")

