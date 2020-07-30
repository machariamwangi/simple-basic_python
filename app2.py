import random

for i in range(3):
   print(random.randint(10, 20))

members = ['John', 'Mark', 'Mash', 'Daniel']
leader = random.choice(members)

print("member", leader)

