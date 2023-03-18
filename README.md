# PresentationRepo

Thanks for your interest in our project! 
You will find here the codes we used for each of the algorithmic approaches we used, together with the data we used, in the Anonimized_data folder.

Data used in each method are (hopefully) included in each methods' folder.

See below for a short explanation of each methods we employed!

### Approximate Entropy (ApEn):
Sample entropy is a close estimation of approximate entropy. The Approximate Entropy method uses the python pyentrp library to calculate entropy scores for each drawing. It then plots the data to show the relation between dominant and non-dominant hand with their associated entropy scores.

### Transfer learning with Convolutional Neural Networks (CNNs):
Neural networks are mathematical functions which learn patterns from semi-automatically analyzing and adjusting itself upon given massive amounts of data.
Convolutional neural networks (CNN) were specifically designed to take in images and identify invariant features through shifts, rotation or adjustment such as brightness.
Convolution and pooling layers are combined to extract important features in the images, which are then used to classify images into categories.

Our code for CNN uses 3 publicly avaialble models: ResNet50, MobileNetV3-Small and Large. We plan to test out many more models and see which ones are best performing!

For data processing, we first took the json data formats we obtained from our website, Neuroprior.com.
Then, a code (also included in the folder CNN_Transfer_Learning) was used to generate images by rendering the json data.
Finally, we manually selected out images that seem relevant to our training and were used.


See the actual codes in the jupyter notebook for further details! You might need some knowledge of ML and Python Keras to be able to understand it. 

To run the code and see the result, import the whole code into google collaboration might be easiest. Then, find the 4th code cell, and adjust the address for the different folders to the right ones, using the data provided in the CNN_Transfer_Learning folder.

### Statistical Inference:
To come!!