"""
A Python script which aims to see if our transfer-learning last layer is capable of
extracting some patterns in the data.

In our approach, we apply transfer-learning to ResNet50, and instead of a 1000 fc layer
which follows the last global average pooling layer in the original model, we simply connect
a dense network which takes all inputs and outputs a single value, which is passed through 
a sigmoid to be interpreted as probability of the image being a dominant / non-dominant hand drawing.

The last average pooling layer output is in the shape 
(batch_size, 2048)
where the 2048 outputs are each results of average pooling after applying the 2048 filters
which should reflect the degree of presence for the 2048 "features" captured by each filter.

We wanted to visualize how data in our dataset cluster together, and whether the division is 
clear between dominant and non-dominant hands.
If those 2048 "features" can be clustered and we can reduce dimensionality, it will be possible
to visualize our result. This is what we explore in this Python script.

General idea:
1) make a dataset which holds all data used in this experiment
2) pass these data through the trained network and spit out all data at the last layer before dense layer
3) store all those data into a csv? Using pandas?
4) Then do something with t-SNE to visualize the result into lower dimensions.
"""

"""
Model building code:

base_model = ("resnet50", tf.keras.applications.resnet50.ResNet50(
        input_shape=(224, 224, 3),
        include_top=False,
        weights='imagenet'
    ))

inputs = Input(shape=(224, 224, 3)) #changed
x = base_model(inputs)
x = GlobalAveragePooling2D()(x)
outputs = Dense(1, activation="sigmoid")(x)

model = Model(inputs=inputs, outputs=outputs)

opt = keras.optimizers.Adam(learning_rate=0.0005)
model.compile(optimizer=opt, loss="binary_crossentropy", metrics=["accuracy"])
"""
