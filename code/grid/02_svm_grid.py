#!/usr/bin/env python3

import numpy as np

UTILS = '../'
import sys
sys.path.append(UTILS)
# Custom imports
from utils import read_data, write_data, metrics, submit
from sklearn.svm import SVC
from param_config import config
import chocolate as choco
from utils import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
np.random.seed(config.set_seed)


TOTAL_RUNS = 5000
c_d = np.logspace(-4, 6, TOTAL_RUNS)
g_d = np.logspace(-5, 6, TOTAL_RUNS)

param_grid = {"C": choco.log(-4, 6, base=10),
              "gamma": choco.log(-5, 6, base=10)}


def model_train(x_train, y_train, x_val, y_val, params):
    svc = SVC(kernel='rbf', verbose=True, **params)
    svc.fit(x_train, y_train)
    y_hat = svc.predict(x_val)

    f1 = metrics(y_val, y_hat)
    return -f1


def split(X, y):
    x_train, x_val, y_train, y_val = train_test_split(X, y, stratify=y, test_size=config.train_val_split_pct)
    return x_train, y_train, x_val, y_val


if __name__ == '__main__':
    num_cols = ['amount_tsh', 'gps_height', 'population', 'total_missing', 'longitude', 'latitude']
    train_x = read_data(config.d_xtrain)
    train_y = read_data(config.d_ytrain)
    test_x = read_data(config.d_xtrain)

    train_x = train_x[num_cols]
    test_x = test_x[num_cols]

    scaler = StandardScaler(with_mean=True, with_std=True)
    scaler.fit(train_x)

    train_x = scaler.transform(train_x)
    test_x = scaler.transform(test_x)

    x_train, y_train, x_val, y_val = split(train_x, train_y)

    conn = choco.MongoDBConnection("mongodb://localhost:27017/")
    sampler = choco.Bayes(conn, param_grid, clear_db=True)
    token, params = sampler.next()

    loss = model_train(x_train, y_train, x_val, y_val, params)
    sampler.update(token, loss)
