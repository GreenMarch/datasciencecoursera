from random import choices
# population = [1, 2, 3, 4, 5, 6]
# weights = [0.1, 0.05, 0.05, 0.2, 0.4, 0.2]

population = ["A", "B","C"]
weights = [0.2, 0.5, 0.3]

million_samples = choices(population, weights, k=10**3)
from collections import Counter
c = Counter(million_samples)
print(c)
# Counter({5: 399616, 6: 200387, 4: 200117, 1: 99636, 3: 50219, 2: 50025})
"""
print(choices(population, weights))
print(choices(population, weights))
print(choices(population, weights))
print(choices(population, weights))
print(choices(population, weights))
print(choices(population, weights))
print(choices(population, weights))
print(choices(population, weights))
print(choices(population, weights))
print(choices(population, weights))
print(choices(population, weights))
print(choices(population, weights))
"""