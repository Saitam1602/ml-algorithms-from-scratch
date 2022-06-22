'''
Author: Matias Maiorano
Date: 22/06/2022
Description: k_means function from scratch
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import os,sys

'''
Piccolo recap dell'algoritmo.

Ci sono 3 step:

* __Inizializzazione__ - $k$ Genero i centroidi in modo casuale
* __Assegnamento__ - Si generano $k$ cluster assegnando ogni punto al centroide più vicino
* __Update__ - Il baricentro di ogni cluster diventa il nuovo centroide

_Assegnamento_ e _Update_ si ripetono fino a convergenza.

* __Convergenza__ - Nessun punto viene assegnato ad un cluster diverso rispetto all'assegnamento precedente.
'''

def k_means(df, k = 3, max_iter = 100, return_center=False):
    
    old_cluster = None
    
    ## Per non allungare troppo il tempo di esecuzione
    for _ in range(max_iter):
    
    
        # __Convergenza__
        ## Stop algoritmo quando i cluster non cambiano alla nuova iterazione
        if old_cluster is not None:
            if np.array_equal(old_cluster, cluster):
                if return_center:
                    return classes, cluster
                else:
                    return classes
        
        
        # __Inizializzazione__
        ## Generazione random dei cluster alla prima iterazione
        if _ == 0:
            cluster = []
            # Controllo che i primi cluster non siano uguali
            positions = [] # per non fare scegliere 2 cluster uguali
            pos = random.randint(0,len(df['x'])-1) 
            for cont in range(k):
                while pos in positions:
                    pos = random.randint(0,len(df['x'])-1) 
                if pos not in positions:
                    positions.append(pos)
                cluster.append([df['x'][pos], df['y'][pos]])

            cluster = np.array(cluster)

        
        # __Assegnamento__
        ## Calcolo distanze, distanze minime
        distances = []
        for cont in range(k):
            # print(len(cluster), cluster)
            distances.append(np.sqrt(((df['x']-cluster[cont][0])**2) + ((df['y']-cluster[cont][1])**2)))
        distances=np.array(distances)
        min_distances = np.min(distances, axis=0)
        
        
        ## Generazione classi
        classes = []
        for col in range(len(min_distances)):
            row_done = False # Per non duplicare i valori
            for class_ in range(k):
                if min_distances[col] == distances[class_][col]:
                    if row_done == False:
                        row_done = True
                        classes.append(class_)
        
        cluster_unique_classes = set(classes) 
        classes = np.array(classes)
        
        
        # __Update__
        ## Valori minimi per assegnare i nuovi centri
        mean_values = []
        for cont in cluster_unique_classes:
            new_cluster = [0,0] # x,y
            div = 0
            for subcont in range(len(classes)):
                if cont == classes[subcont]:
                    new_cluster[0] += df['x'][subcont]
                    new_cluster[1] += df['y'][subcont]
                    div +=1
            mean_values.append([new_cluster[0]/div, new_cluster[1]/div])
        old_cluster = cluster.copy()
        cluster = np.array(mean_values)
        
    if return_center:
        return classes, cluster
    else:
        return classes


if __name__ == '__main__':
    ## TEST
    os.system('cls')
    random.seed(0)

    df = pd.DataFrame({
        'x': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
        'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
    })

    classes, cluster = k_means(df, k = 5, max_iter=100000, return_center=True)

    plt.scatter(df['x'], df['y'], alpha=.5, s=200,c=classes,edgecolor='k')
    colormap = list(set(classes))
    plt.scatter(cluster[:,0],cluster[:,1], alpha=1, s=50, c=colormap, edgecolor='black')
    plt.show()