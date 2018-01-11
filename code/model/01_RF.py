#!/usr/bin/env python3

import sys
sys.path.append("../")
from param_config import config
from utils import read_data
from utils import write_data
import numpy as np
from sklearn.ensemble import RandomForestClassifier
np.random.seed(config.set_seed)


def model(X, y, samples=10000):
    X, y = X[:samples], y[:samples]

    model = RandomForestClassifier(n_estimators=40, min_samples_leaf=3, n_jobs=-1, oob_score=True)
    print(X.dtypes)
    model.fit(X, y)
    exit()
    return model


if __name__ == '__main__':
    # train data set
    train_x = read_data(config.c_xtrain)
    train_y = read_data(config.a_ytest)

    # test data set
    test_x = read_data(config.c_xtest)

    # get drop date_recorded
    drop_col = ['date_recorded']
    train_x = train_x.drop(drop_col, axis=1)
    test_x = test_x.drop(drop_col, axis=1)

    model = model(train_x, train_y)
    print(model)
    #print(train_x.columns)
    #print(test_x.dtypes)