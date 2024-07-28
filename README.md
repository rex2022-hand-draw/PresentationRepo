# Classification of hand drawings using machine learning algorithms!

Thanks for your interest in our project! You will find here:
* **code** for each algorithmic approaches
* **data** we used in our project, in the *Anonimized_data* folder.
* [Presentation Link](https://www.canva.com/design/DAFZwoDS9fc/wXBiEtTuZ2Y5Zu4d5BAPzw/edit?utm_content=DAFZwoDS9fc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

Data used in each method are (hopefully) included in each methods' folder.

See below for a short explanation of each methods we employed!

### Approximate Entropy (ApEn):
Sample entropy is a close estimation of approximate entropy. The Approximate Entropy method uses the python pyentrp library to calculate entropy scores for each drawing. It then plots the data to show the relation between dominant and non-dominant hand with their associated entropy scores.

### Transfer learning with Convolutional Neural Networks (CNNs):
Neural networks semi-automatically learn patterns from massive amounts of data.

**Convolutional neural networks (CNN)** were specifically designed for sequential input, such as images, to identify invariant features through shifts, rotation or adjustment such as brightness.
Convolution and pooling layers extract important features in images, which are then used to classify them into categories.

Our code uses **3 publicly avaialble models**:
* ResNet50
* MobileNetV3-Small
* MobileNetV3-Large 

We plan to test more models to look for best performance!

For data processing, we took **json data** obtained from **Neuroprior.com**, which was then **rendered into images** through code also included in CNN_Transfer_Learning.
Finally, we **manually selected images** relevant to our training.


See annotations in the jupyter notebook for further details! Some background knowledge of machine learningand Python Keras might be needed. 

The code is runnable by importing it into Google Colaboratory. Find the 4th code cell, and adjust paths, using the data provided in the CNN_Transfer_Learning folder.

### Statistical Inference:
To come!!
