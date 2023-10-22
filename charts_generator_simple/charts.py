import matplotlib.pyplot as plt
# import numpy as np


def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 346, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pieses.png')
    plt.close()

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
    ax.set_title("perras") #title
    ax.legend("perrassss") #legends
    plt.savefig('pplot.png') #save
    plt.close()

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
