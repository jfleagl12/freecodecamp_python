# import random
#
# print("WELCOME")
#
# r1=random.randint(1,6)
#
# while True:
#
#     print("YOU ROLLED THE DICE",r1)
#
#     r1=random.randint(1,6)
#
#     user_input=(input("ENTER Y OR N:"))
#
#     if user_input=="N":
#
#         break
#
#     else:
#
#         continue
#

import random

min = 1
max = 100

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":

  print("Rolling the dice...")

  print("The values are....")

  print (random.randint(min, max))

  roll_again = input("Roll the dice again?")
