#!/usr/bin/env python3

import sys
sys.path.append("../")
from param_config import config
from utils import read_data
from utils import write_data
import numpy as np
from sklearn.cluster import KMeans
np.random.seed(config.set_seed)


def kmeans(x_train, x_test):
    header_str = 'kmeans_lat_long'
    lat_long = ['latitude', 'longitude']
    X = x_train[lat_long]

    print('#### Generating Clusters ####')
    kmean_model = KMeans(n_clusters=config.no_clusters)
    kmean_model.fit(X)
    x_train[header_str] = kmean_model.predict(X)
    x_test[header_str] = kmean_model.predict(x_test[lat_long])
    return x_train, x_test


if __name__ == '__main__':
    train_x = read_data(config.b_xtrain)
    test_x = read_data(config.b_xtest)

    x_train, x_test = kmeans(train_x, test_x)

    print('#### Writing Pickle 03: Kmeans ####')
    write_data(config.c_xtrain, train_x)
    write_data(config.c_xtest, test_x)


# Try https://hdbscan.readthedocs.io/en/latest/