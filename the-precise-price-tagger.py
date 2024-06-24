#Create a program that rounds off prices to a user-friendly format. Will utilize round()
import math
print("Please enter the price of your items: ")
price = input().split()
#price = float(price)

prices = []

for each in price:
    prices.append(each)
    
new_prices = [float(i) for i in prices]
print(new_prices)

#print(prices)

total = sum(new_prices)
print(total)

#print(round(price, 2))
#print(math.ceil(price))
#print(math.floor(price))

