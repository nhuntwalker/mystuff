import numpy as np
import random as rand

n = input('How many people are we starting with?\t')

r = np.random.random(n)
parents = np.zeros(n, int)
MALE, FEMALE = 1,2
parents[r < male_portion] = MALE
parents[r >= male_portion] = FEMALE

males = len(parents[parents==MALE])
females = len(parents) - males
couples = min(males, females)

fertility = 1.0
n = int(fertility*couples) # couples that get a child

# the next generation, one child per couple:
r = np.random.random(n)
children = zeros(n, int)
children[r < male_portion] = MALE
children[r >= male_portion] = FEMALE


