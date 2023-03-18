import os

import apEnCalc
import tags


def accuracy(folder_path, threshold):
    numCorrect = 0
    numIncorrect = 0

    for file in os.scandir(folder_path):
        if file.is_file():
            apEnValue = apEnCalc.apEn(file.path)
            if apEnValue is not None:
                hand = tags.hand_dominance(file.path)
                if hand == "dominant":
                    if apEnValue < threshold:
                        numCorrect += 1
                    else:
                        numIncorrect += 1
                elif hand == "non-dominant":
                    if apEnValue > threshold:
                        numCorrect += 1
                    else:
                        numIncorrect += 1

    return float(numCorrect) / (numCorrect + numIncorrect)