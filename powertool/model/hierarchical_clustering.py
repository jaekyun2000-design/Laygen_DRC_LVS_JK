from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import scipy.cluster.hierarchy as sch
import pandas as pd
import numpy as np



if __name__ == '__main__':

    X = np.array([[1,3,5],[2,4,6],[44,14,0]])
    X = pd.read_csv('./gds_test.csv')

    linked = linkage(X,'single')

    plt.figure(figsize=(10,7))
    dendrogram(linked,orientation='top',distance_sort='descending',show_leaf_counts=True)
    plt.show()


    dend = dendrogram(linked)

    from scipy.cluster.hierarchy import fcluster

    cut_tree = fcluster(linked,t=1,criterion='distance')
    cut_tree