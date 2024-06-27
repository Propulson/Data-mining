import matplotlib.pyplot as plt
from random_walk import RandomWalk
#build
#use while
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    point_numbers = range(rw.number_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    ax.scatter(0, 0, c='green', edgecolors='none', s=1)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    #delete x, y
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('Do you want to continue? (y/n) ')
    if keep_running == 'n':
        break

