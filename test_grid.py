import itertools as it
from itertools import combinations




# Grid size = 2 x 2
# Run only if you can wait more than one hour to let this big grid process

possible_combinations = {}

coordinates = []

for i in range(2):
    for j in range(2):
        coordinates.append((i,j))



for i in range(1, 4):
    # " i " means that for example, in a grid of 2 x 2, how many circled numbers are present.
    a = list(combinations(coordinates, i))

    possible_combinations[i] = a

#print(possible_combinations)

b = {}

for key, values in possible_combinations.items():

    for i in values:

      b[i] =  [x for x in it.product(range(4), repeat=key)]

c = 0
for  values in b.values():


    c = c + (len(values))

print(c)



#================================================================================================

# Grid size = 3 x 3
# Run only if you can wait more than one hour to let this big grid process

possible_combinations = {}

coordinates = []

for i in range(3):
    for j in range(3):
        coordinates.append((i,j))



for i in range(1, 9):
    # " i " means that for example, in a grid of 3 x 3, how many circled numbers are present.
    a = list(combinations(coordinates, i))

    possible_combinations[i] = a

#print(possible_combinations)

b = {}

for key, values in possible_combinations.items():

    for i in values:

      b[i] =  [x for x in it.product(range(9), repeat=key)]

c = 0
for  values in b.values():


    c = c + (len(values))

print(c)

#================================================================================================

# Grid size = 4 x 4
# Run only if you can wait more than one hour to let this big grid process

possible_combinations = {}

coordinates = []

for i in range(4):
    for j in range(4):
        coordinates.append((i,j))



for i in range(1, 16):
    # " i " means that for example, in a grid of 4 x 4, how many circled numbers are present.
    a = list(combinations(coordinates, i))

    possible_combinations[i] = a

#print(possible_combinations)

b = {}

for key, values in possible_combinations.items():

    for i in values:

      b[i] =  [x for x in it.product(range(16), repeat=key)]

c = 0
for  values in b.values():


    c = c + (len(values))


print(c)
#================================================================================================

# Grid size = 5 x 5
# Run only if you can wait more than one hour to let this big grid process

possible_combinations = {}

coordinates = []

for i in range(5):
    for j in range(5):
        coordinates.append((i,j))



for i in range(1, 25):
    # " i " means that for example, in a grid of 5 x 5, how many circled numbers are present.
    a = list(combinations(coordinates, i))

    possible_combinations[i] = a

#print(possible_combinations)

b = {}

for key, values in possible_combinations.items():

    for i in values:

      b[i] =  [x for x in it.product(range(25), repeat=key)]

c = 0
for  values in b.values():


    c = c + (len(values))

print(c)

#================================================================================================

# Grid size = 6 x 6
# Run only if you can wait more than one hour to let this big grid process

possible_combinations = {}

coordinates = []

for i in range(6):
    for j in range(6):
        coordinates.append((i,j))



for i in range(1, 36):
    # " i " means that for example, in a grid of 6 x 6, how many circled numbers are present.
    a = list(combinations(coordinates, i))

    possible_combinations[i] = a

#print(possible_combinations)

b = {}

for key, values in possible_combinations.items():

    for i in values:

      b[i] =  [x for x in it.product(range(36), repeat=key)]

c = 0
for  values in b.values():


    c = c + (len(values))

print(c)

#================================================================================================

# Grid size = 7 x 7
# Run only if you can wait more than one hour to let this big grid process

possible_combinations = {}

coordinates = []

for i in range(10):
    for j in range(10):
        coordinates.append((i,j))



for i in range(1, 100):
    # " i " means that for example, in a grid of 7 x 7, how many circled numbers are present.
    a = list(combinations(coordinates, i))

    possible_combinations[i] = a

#print(possible_combinations)

b = {}

for key, values in possible_combinations.items():

    for i in values:

      b[i] =  [x for x in it.product(range(49), repeat=key)]

c = 0
for  values in b.values():


    c = c + (len(values))

print(c)

#================================================================================================

# Grid size = 10 x 10
# Run only if you can wait more than one hour to let this big grid process

possible_combinations = {}

coordinates = []

for i in range(8):
    for j in range(8):
        coordinates.append((i,j))



for i in range(1, 64):
    # " i " means that for example, in a grid of 8 x 8, how many circled numbers are present.
    a = list(combinations(coordinates, i))

    possible_combinations[i] = a

#print(possible_combinations)

b = {}

for key, values in possible_combinations.items():

    for i in values:

      b[i] =  [x for x in it.product(range(64), repeat=key)]

c = 0
for  values in b.values():


    c = c + (len(values))


print(c)





#================================================================================================

# Grid size = 9 x 9
# Run only if you can wait more than one hour to let this big grid process

possible_combinations = {}

coordinates = []

for i in range(9):
    for j in range(9):
        coordinates.append((i,j))



for i in range(1, 81):
    # " i " means that for example, in a grid of 9 x 9, how many circled numbers are present.
    a = list(combinations(coordinates, i))

    possible_combinations[i] = a

#print(possible_combinations)

b = {}

for key, values in possible_combinations.items():

    for i in values:

      b[i] =  [x for x in it.product(range(81), repeat=key)]

c = 0
for  values in b.values():


    c = c + (len(values))


print(c)







#================================================================================================

# Grid size = 10 x 10
# Run only if you can wait more than one hour to let this big grid process

possible_combinations = {}

coordinates = []

for i in range(10):
    for j in range(10):
        coordinates.append((i,j))



for i in range(1, 100):
    # " i " means that for example, in a grid of 10 x 10, how many circled numbers are present.
    a = list(combinations(coordinates, i))

    possible_combinations[i] = a

#print(possible_combinations)

b = {}

for key, values in possible_combinations.items():

    for i in values:

      b[i] =  [x for x in it.product(range(100), repeat=key)]

c = 0
for  values in b.values():


    c = c + (len(values))



print(c)













