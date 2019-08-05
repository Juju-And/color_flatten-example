import numpy as np
import time
import sys

from skimage import io
from sklearn.cluster import KMeans

try:
    list_of_args = sys.argv[1:]

    result = 0

    for arg in list_of_args:
        imagePath = arg

        url = 'images/{}'.format(imagePath)
        original = io.imread(url)
        n_colors = 6

        arr = original.reshape((-1, 3))
        kmeans = KMeans(n_clusters=n_colors, random_state=42).fit(arr)
        labels = kmeans.labels_
        centers = kmeans.cluster_centers_
        less_colors = centers[labels].reshape(original.shape).astype('uint8')

        io.imsave('results/result_{}.png'.format(result), arr=less_colors)
        result += 1
except IOError:
    print("Not valid input file name")
