# //////////////print() function ////////////////


print("hello world..........")

# output : hello world..........

# ////////////////////variables////////////////

a = 1
b = 20
print(a,b)
# output : 1 20



a = 1
b = 20
print(a+b)

# output: 21


name = "kavita"
print('hello',name,'i hope you are doing well')
# output: hello kavita i hope you are doing well




# //////////////assignment//////////


# Assignment 1: Variables aur Data Types Practice
# Ek program banao jismein ye variables banayein:
# name (string),
# age (integer),
# is_student (boolean - True ya False).
# In sab ko print() function se screen par show karo.


name = 'kavita'
age = 19
is_student = True

print('Name:' , name)
print('Age:' , age)
print('is_student:' , is_student)

# output: Name: kavita
# Age: 19
# is_student: True


# ////////////// assignment 2 ////////////////

num1 = 20
num2 = 30

print(num1 + num2)   #output : 50
print(num1 - num2)   #output: -10
print(num1 * num2)   #output: 600
print(num1 / num2)   #output: 0.6666666666666666666666





# Simple Receipt Generator

item1 = "Notebook"
price1 = 150

item2 = "Pen"
price2 = 50

item3 = "Bag"
price3 = 1200

# Calculate total
total = price1 + price2 + price3

# Print receipt
print("🧾 Shopping Receipt")
print("--------------------------")
print(f"Item 1: {item1} - Rs.{price1}")
print(f"Item 2: {item2} - Rs.{price2}")
print(f"Item 3: {item3} - Rs.{price3}")
print("--------------------------")
print(f"Total Amount: Rs.{total}")
print("--------------------------")