import numpy as np
from skimage import io
from sklearn.cluster import KMeans

original = io.imread('img/yosemite.jpg')
n_colors = 3

arr = original.reshape((-1, 3))
kmeans = KMeans(n_clusters=n_colors, random_state=24).fit(arr)
labels = kmeans.labels_
centers = kmeans.cluster_centers_
less_colors = centers[labels].reshape(original.shape).astype('uint8')

io.imshow(less_colors)
io.imsave('img/yosemite_clustered.jpg', less_colors)