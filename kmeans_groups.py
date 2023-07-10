#!/usr/bin/env python3
import sys
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def run_kmeans_clustering(k, mic_csv):
    i = 1
    while os.path.exists("km_groups_{:02d}.csv".format(i)):
        i += 1

# Create output file names with numbered suffixes
    group_filename = "km_groups_{:02d}.csv".format(i)
    centers_filename = "km_centers_{:02d}.csv".format(i)
    scatterplot_filename = "km_plot_{:02d}.png".format(i)

    data = pd.read_csv(mic_csv, header=None)
    f1 = data.iloc[:, 1].values
    f2 = data.iloc[:, 2].values
    names = data.iloc[:, 0].values
    X = np.column_stack((f1, f2))

    kmeans = KMeans(init='k-means++', algorithm="lloyd", n_init="auto", n_clusters=k)
    labels = kmeans.fit_predict(X)
    clusters = kmeans.cluster_centers_

    pd.DataFrame({'name': names, 'class': [str(l).zfill(3) for l in labels]})\
        .to_csv(group_filename, index=False)

    pd.DataFrame({'x': clusters[:, 0], 'y': clusters[:, 1]})\
        .to_csv(centers_filename, index=False)

    plt.figure(1)
    plt.clf()
    plt.scatter(f1, f2, marker='.', s=100, c=labels, cmap='tab20')
    plt.scatter(clusters[:, 0], clusters[:, 1], marker='x', s=50, color='r')
    plt.savefig(scatterplot_filename)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: kmeans_group.py <k> <inputcsv>")
        sys.exit(1)

    k = int(sys.argv[1])
    inputcsv = sys.argv[2]

    run_kmeans_clustering(k, inputcsv)

