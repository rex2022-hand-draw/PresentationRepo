import numpy as np
import matplotlib.pyplot as plt
# from pyeeg import ap_entropy
import pyentrp
from pyentrp import entropy as ent
from PIL import Image
import timeSeries

def apEn(filePath):

    # calculation of 1D time series
    time_series1 = timeSeries.return_time_series(filePath)

    # Calculate SD of the time series
    if time_series1 is None or len(time_series1) == 0:
        return None
    else:
        std_time_series1 = np.std(time_series1)

        sample_entropy1 = ent.sample_entropy(time_series1, 4, 0.2 * std_time_series1)

        # average of all 4 entropy values:
        total = 0
        for i, value in enumerate(sample_entropy1):
            total += value
        average = total / 4

        return average

    # load entropy values


    # print out the entropy values
    # print("Entropy values:")
    # for i, value in enumerate(sample_entropy1):
    #     print("Sample entropy of dimension ", i, " is ", value)

