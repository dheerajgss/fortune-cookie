print("Enjoy the fortune cookie")

import random

lucky_list = ["Success follows you everywhere!","You are the best in what you do.",
"You are a great inspiration to others!","Your talents will help you build a better future",
"You are the life of the party!","You are a true hero", "Learning is a breeze!","You stand for what is right"]

print("\nThe fortune reads: ", random.choice(lucky_list))
x = random.sample(range(1,10), 2)
print("\nYour lucky numbers are: ", x)

print("\nI hope you like this cookie. Happy Hacking!\n")