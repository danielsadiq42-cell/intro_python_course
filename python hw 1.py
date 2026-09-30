day = input("Enter date:")
month = input("Enter month:")
year = input("Enter year:")
print (day + "/" + month + "/" + year)

income = float(input("Enter income:"))
if income < 10000:
    tax = income * 0.08
elif income <= 26000:
    tax = income * 0.12
else:
    tax = income * 0.24
print("Tax:", tax) 

a = int(input("Enter a:"))
b = int(input("Enter b:"))
if a > b:
    print("Error, a must be less than b")
else:
  for i in range(a,b + 1):
    print(i)

number = int(input("Enter a number:"))
for i in range (2, number + 1, 2):
   print(i)

total = 0
while answer:
   price = float(input("Item price:"))
   total = total + price
   answer = input("Have more items? (y/n:)")
   if answer == "n":
     break
print("TOTAL:", total)

