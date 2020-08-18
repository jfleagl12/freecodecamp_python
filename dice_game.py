import random

print("WELCOME")

r1=random.randint(1,6)

while True:

    print("YOU ROLLED THE DICE",r1)

    r1=random.randint(1,6)

    user_input=(input("ENTER Y OR N:"))

    if user_input=="N":

        break

    else:

        continue  
