#!/usr/bin/env python3

import sys
sys.path.append("../")
from param_config import config
from imblearn.over_sampling import RandomOverSampler, SMOTE
from utils import read_data, write_data
import numpy as np
from scipy import stats
np.random.seed(config.set_seed)


def imbalance_split(X, y):
    ros = SMOTE(random_state=config.set_seed)
    X_res, y_res = ros.fit_sample(X, y)
    return X_res, y_res


# Try imbalance learn
if __name__ == '__main__':
    train_x = read_data(config.d_xtrain)
    train_y = read_data(config.d_ytrain)
    X, y = imbalance_split(train_x, train_y)

    write_data(config.e_xtrain, X)
    write_data(config.e_ytrain, y)

