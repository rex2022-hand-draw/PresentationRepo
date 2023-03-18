import matplotlib.pyplot as plt
import numpy as np

def histogram(dominant_data, non_dominant_data):

    # example dataOld for dominant and non-dominant hands
    # dominant_data = [0, 0, 0, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.35, 0.4]
    # non_dominant_data = [0.3, 0.6, 0.9, 1.1, 1.3, 1.6, 2.1, 2.3, 2.5]

    # plot the two histograms

    binwidth = 0.025
    bins = np.arange(min(dominant_data + non_dominant_data), max(dominant_data + non_dominant_data) + binwidth, binwidth)

    plt.hist(dominant_data, bins=bins, alpha=0.5, label='dominant', color='red')
    plt.hist(non_dominant_data, bins=bins, alpha=0.5, label='non-dominant', color='blue')

    # add labels and title
    plt.xlabel('Entropy value')
    plt.ylabel('Count')
    plt.title('Entropy Values for Dominant and Non-Dominant Hands')

    # add legend
    plt.legend()

    # show plot
    plt.xlim(0, 2)
    plt.ylim(0, 4)
    plt.show()


