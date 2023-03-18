import pandas as pd
import numpy as np

def dataTable(dominant_data, non_dominant_data):

    # calculate median, mean, and standard deviation
    dominant_median = np.median(dominant_data)
    dominant_mean = np.mean(dominant_data)
    dominant_std = np.std(dominant_data)
    non_dominant_median = np.median(non_dominant_data)
    non_dominant_mean = np.mean(non_dominant_data)
    non_dominant_std = np.std(non_dominant_data)

    # create a dictionary for the values
    data = {
        'Measurement': ['Median', 'Mean', 'Standard Deviation'],
        'Dominant': [dominant_median, dominant_mean, dominant_std],
        'Non-Dominant': [non_dominant_median, non_dominant_mean, non_dominant_std]
    }

    # create a dataframe from the dictionary
    df = pd.DataFrame(data)

    # set the index
    df = df.set_index('Measurement')

    # print the table
    print(df)



