import random

# Generating random number
# random_number = random.randint(1,10)
# print(random_number)

# Generating random floating point numbers
# num = random.random()
# print(num)

# Heads or Tails Random Algorithm
num = random.randint(0,1)
if num == 0:
    print("Heads")
else:
    print("Tails")

friends = ['Nonso', 'Emmanuel', 'Ezege', 'Michael',]

print(random.choice(friends))

random_number = random.randint(0, len(friends) -1)

print(friends[random_number])