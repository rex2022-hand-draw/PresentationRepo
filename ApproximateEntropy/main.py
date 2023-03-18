import numpy as np
import matplotlib.pyplot as plt
# from pyeeg import ap_entropy
import pyentrp
from pyentrp import entropy as ent
from PIL import Image

import dataTable
import histogram
import tTest
import tags
import timeSeries
import apEnCalc
import os
import accuracy

# file path for one of the images
# filePath = "C:\\Users\\sinku\\PythonProjects\\ApEn2\\dataOld\\1665514649973"

# num = apEnCalc.apEn(filePath)


# folder_path = "./data/"
folder_path = "./newData/"

dom = []
nonDom = []

for file in os.scandir(folder_path):
    if file.is_file():
        apEnValue = apEnCalc.apEn(file.path)
        if apEnValue is not None:
            print(apEnValue)
            hand = tags.hand_dominance(file.path)
            print(hand)
            if hand == "dominant":
                dom.append(apEnValue)
            elif hand == "non-dominant":
                nonDom.append(apEnValue)

histogram.histogram(dom, nonDom)
dataTable.dataTable(dom, nonDom)
# print(np.mean(dom))
# print(np.mean(nonDom))

tTest.t_test(dom, nonDom)

# mean-based threshold
dominant_mean = np.mean(dom)
non_dominant_mean = np.mean(nonDom)
threshold = (non_dominant_mean + dominant_mean) / 2
# print("Mean threshold: " + str(threshold))
acc = accuracy.accuracy(folder_path, threshold)
print("Accuracy (mean): " + str(acc))

# median-based threshold
dominant_median = np.median(dom)
non_dominant_median = np.median(nonDom)
threshold = (non_dominant_median + dominant_median) / 2
# print("Median threshold: " + str(threshold))
acc2 = accuracy.accuracy(folder_path, threshold)
print("Accuracy (median): " + str(acc2))







