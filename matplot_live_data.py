from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from itertools import count

ind = count()
# lists to maintain avalues
x = []
y1 = []
y2 = []

# to have an animation
def animate(i):

    # update x values by adding 1 unit
    x.append(next(ind))
    # to update y1 and y2
    y1.append(random.uniform(1, 11))
    y2.append(random.uniform(1, 11))

    # clear axes
    plt.cla()

    # plot the data
    plt.plot(x, y1, label='Num 1', marker='*', linestyle='-', color='blue')
    plt.plot(x, y2, label='Num 2', marker='*', linestyle='', color='red')

    # display the labels
    plt.legend(loc='upper left')

    # declare the title
    plt.title('Two Random Nums (1.0-10.0)')

# call animate function every 1 second 
a = FuncAnimation(plt.gcf(), animate, interval=1000) # 1000 = 1 second

# show the plot
plt.show()

