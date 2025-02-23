import random
secret = random.randint(1, 10)

for i in range(3):  #  3 attempts
    user = int(input("Enter your number: "))

    if user == secret:
        print("🎉 Correct number in", i + 1, "attempts! The number was", secret,"wohooooooo")
        break  
    elif user < secret:
        print("Your guess is too low..")
    else:
        print("Your guess is too high..")


else:
    print("😢 Game Over! The correct number was", secret, "and your attempts ",i+1)
