import os; os.system('cls')
from k_means import K_means
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import make_moons

if __name__ == '__main__':
    x, y = make_moons()
    # print(x.shape)
    model = K_means(return_center=True, k=3)
    model.fit(x)
    classes, centroids = model.predict()
    plt.scatter(x[:,0],x[:,1], c=classes)
    plt.scatter(centroids[:,0], centroids[:,1], c=['red'], alpha=.3)
    plt.show()
    # print(x[0].shape)