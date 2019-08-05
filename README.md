# Color_flatten-example

The application is based on centroid algorithm. Centroid it is a point within the area/shape/polygon,
which lies in this shape and represents its center. Centroid algorithm is one of data clustering algorithms,
method of, so called, unsupervised learning – elements are grouped into relatively homogeneous classes.
In case of deep learning algorithm method could be used in other way than for its intended purpose (classification into
clusters), but to create so-called filters (convolution kernels, dictionaries). For example, to recognize images in the centroid
algorithm are given small For example, to recognize images in the centroid algorithm are given small random pieces of images of
the training sample, say, the size of 16x16 in the form of a linear vector, each element of which encodes the brightness
of its point.
The number of clusters k is set to be large, for example, 256. The trained k-average method, under certain conditions,
produces the centres of clusters (centroids), which are convenient bases on which to decompose any input image.

Inside the code can be found a variable called ‘n_colors’, which is used to define how many clusters is going to be used to
rewrite the input picture. By clustering, we understand pieces of training sample. The more pieces to train the model,
the better reproduction as a result.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install all required modules running pip with the provided file:

```
pip install requirements.txt
```

### Installing

First step is to set the number of clusters by providing it within n_colors variable.

After the script can be run, but should be provided with the name of file/files to be reproduced.

```
$ python3 color_flatten_script.py <file1_name> <file2_name> ...
```

Ready reproductions can be found in the results folder.