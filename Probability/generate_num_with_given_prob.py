from random import choices
# population = [1, 2, 3, 4, 5, 6]
# weights = [0.1, 0.05, 0.05, 0.2, 0.4, 0.2]

population = ["A", "B","C"]
weights = [0.2, 0.5, 0.3]

million_samples = choices(population, weights, k=10**3)

from collections import Counter
c = Counter(million_samples)
print(c.most_common())
print(sorted(c.items()))
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