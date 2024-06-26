import matplotlib.pyplot as plt
from random_walk import RandomWalk
#build
rw = RandomWalk()
rw.fill_walk()
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
