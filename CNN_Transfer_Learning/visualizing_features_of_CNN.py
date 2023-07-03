"""
This scripts aim to realize visualiation of CNN feature maps.
There are quite a few ways in which we can visualize what features CNNs pay attention
to when doing classifications. We want to apply that specifically to our 
performant transfer-learning version of ResNet50 to elucidate what exactly the CNNs
look at.
"""

from vis.visualization import visualize_cam

# This corresponds to the Dense linear layer.
for class_idx in np.arange(10): 
 indices = np.where(val_y[:, class_idx] == 1.)[0]
 idx = indices[0]

f, ax = plt.subplots(1, 4)
 ax[0].imshow(val_x[idx][..., 0])
 
for i, modifier in enumerate([None, 'guided', 'relu']):
    grads = visualize_cam(model, layer_idx, filter_indices=class_idx, 
    seed_input=val_x[idx], backprop_modifier=modifier) 
    if modifier is None:
        modifier = 'vanilla'
    ax[i+1].set_title(modifier) 
    ax[i+1].imshow(grads, cmap='jet')