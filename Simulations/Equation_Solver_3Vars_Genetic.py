"""
AI Neural Genetic Algorithm that solves any type of algebraic equation in 3 variables
Please, input your equation inside the return statement on line 11
"""
import random
import matplotlib.pyplot as plt

best_fitness_values = []

def foo(x,y,z):
    return (8 * x + 3 * y + 5 * z) / 4 * x * y * z

def fitness(x,y,z):
    ans = foo(x,y,z)
    if ans == 0:
        return 9999
    else:
        return abs(1/ans)

# generating sollutions
solutions = []
for s in range(1000):
    solutions.append((random.uniform(0, 100000), random.uniform(0, 100000), random.uniform(0, 100000)))

for i in range(10000):
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append((fitness(s[0], s[1], s[2]),s))
    rankedsolutions.sort()
    rankedsolutions.reverse()

    best_fitness_values.append(rankedsolutions[0][0])

    print(f"--- Generation {i} best solutions ---")
    print(rankedsolutions[0])

    if rankedsolutions[0][0] > 99:
        break

    bestsolutions = rankedsolutions[:100]

    elements=[]

    for s in bestsolutions:
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])

    newGen = []
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(0.99, 1.01)
        e2 = random.choice(elements) * random.uniform(0.99, 1.01)
        e3 = random.choice(elements) * random.uniform(0.99, 1.01)
        newGen.append((e1, e2, e3))

    solutions = newGen

print(f"The solution is: x = {rankedsolutions[0][1][0]:.3f}, y = {rankedsolutions[0][1][1]:.3f}, z = {rankedsolutions[0][1][2]:.3f}")


plt.plot(best_fitness_values)
plt.xlabel('Generation')
plt.ylabel('Best Fitness Value')
plt.title('Fitness Progression Over Generations')
plt.grid(True)
plt.show()




