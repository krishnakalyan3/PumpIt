#!/usr/bin/env python3

import sys
sys.path.append("../")
from sklearn.decomposition import PCA
from param_config import config
from utils import read_data
from utils import write_data
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

np.random.seed(config.set_seed)

num_cols = ['amount_tsh', 'gps_height', 'population', 'total_missing']


# Scale and Fit
# standard mean and unit variance scale
def pca(x_train, x_test):
    std_clf = make_pipeline(StandardScaler(), PCA(n_components=config.pca_components))
    std_clf.fit(x_train)
    train_pca = std_clf.transform(x_train)
    test_pca = std_clf.transform(x_test)
    return train_pca, test_pca


if __name__ == '__main__':
    train_x = read_data(config.d_xtrain)
    test_x = read_data(config.d_xtest)
    train_pca, test_pca = pca(train_x[num_cols], test_x[num_cols])

    print('#### Writing Pickle 1: PCA ####')
    write_data(config.pca_xtrain, train_pca)
    write_data(config.pca_xtest, test_pca)
