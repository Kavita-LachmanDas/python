
# ////////////calculator//////////////

user1 = int(input("Enter Your First Number: "))
user2 = int(input("Enter Your Second Number: "))
operators = input('Enter Your Operator:  ')


if operators == "+":
    print(user1 + user2)
elif operators == "-":
    print(user1 + user2)
elif operators == "*":
    print(user1 * user2)    
elif operators == "/":
    print(user1 / user2)   
elif operators == "%":
    print(user1 % user2)  
elif operators == "//":
    print(user1 // user2)       
else: 
    print('Invalid Operation')


# for i in range(1,11):
#     print("2 *" , i , "= " , i*2)


# ///////////table in accending order///////////////

user = int(input("Enter the Table number which you want to print......."))
for i in range(1,11):
    print(user , "*" , i , "=" ,  i*user)




# ///////////table in deccending order///////////////
user = int(input("Enter the Table number which you want to print......."))
for i in range(10,0,-1):
    print(user , "*" , i , "=" ,  i*user)