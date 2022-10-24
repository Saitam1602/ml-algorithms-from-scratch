import numpy as np
import random


class K_means:
    def __init__(self, k=3, max_iter=100, return_center=False):
        self.x = None
        self.k = k
        self.max_iter = max_iter
        self.return_center = return_center

    def fit(self, x):
        self.x = x

    def predict(self):

        old_cluster = None

        for iteration in range(self.max_iter):

            # __Convergenza__
            if old_cluster is not None:
                if np.array_equal(old_cluster, cluster):
                    if self.return_center:
                        return classes, cluster
                    else:
                        return classes

            # __Inizializzazione__
            if iteration == 0:
                cluster = np.array([])
                positions = np.array([])

                pos = random.randint(0, self.x.shape[0]-1)
                for cont in range(self.k):
                    while pos in positions:
                        pos = random.randint(0, self.x.shape[0]-1)
                    if pos not in positions:
                        positions = np.append(positions, pos)
                    cluster = np.append(cluster, self.x[pos])
                cluster = cluster.reshape(-1, self.x[0].shape[0])

            # __Assegnamento__
            distances = np.array([])
            for x in self.x:
                for cont in range(self.k):
                    distance = np.sqrt(np.sum((x-cluster[cont])**2))
                    distances = np.append(distances, distance)
            distances = distances.reshape(-1, self.k)
            classes = np.argmin(distances, axis=1)

            # __Update__
            old_cluster = cluster
            cluster = np.array([])
            for class_ in np.unique(classes):
                mean_values = np.array([])
                for row in range(self.x.shape[0]):
                    if class_ == classes[row]:
                        mean_values = np.append(mean_values, self.x[row])
                mean_values = mean_values.reshape(-1, self.x.shape[1])
                one_cluster = np.mean(mean_values, axis=0)
                cluster = np.append(cluster, one_cluster)
            cluster = cluster.reshape(-1, self.x.shape[1])

        if self.return_center:
            return classes, cluster
        else:
            return classes
