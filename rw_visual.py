import matplotlib.pyplot as plt

# Importing RandomWalk() from random_walk.py
from random_walk import RandomWalk

# Make a random walk.

rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk

plt.style.use('classic')
fig, ax = plt.subplots()

ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
