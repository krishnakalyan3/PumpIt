#!/usr/bin/env python3

from sklearn.preprocessing import Imputer
import sys
sys.path.append("../")
import pandas as pd
from param_config import config
from sklearn.preprocessing import LabelEncoder
from utils import read_data
from utils import write_data
from mapping import target_mapping
import numpy as np
np.random.seed(config.set_seed)


def imputer(x_train, x_test):
    # Unused
    # https://groups.google.com/forum/#!msg/jpmml/sooCGcGMpnc/x-EkjOr2BAAJ

    imp = Imputer(missing_values='NaN', strategy=config.imputation_stratergy, axis=0)
    imp.fit(x_train)
    train = imp.transform(x_train)
    test = imp.transform(x_test)
    return train, test


def label_encoding(x_train, x_test, impute_data):

    lbl = LabelEncoder()
    for c in x_train.columns:
        if x_train[c].dtype == 'object':

            print('###### Encoding {} #####'.format(c))
            if c in impute_data:
                x_train[c], x_test[c] = x_train[c].fillna(impute_data[c]), x_test[c].fillna(impute_data[c])

            raw_data = pd.concat([x_train[c], x_test[c]])
            lbl.fit(raw_data.values)
            x_train[c] = lbl.transform(list(x_train[c].values))
            x_test[c] = lbl.transform(list(x_test[c].values))

    return x_train, x_test


def most_frequent(x_train):
    na_cols = {}
    for c in x_train.columns:
        if x_train[c].isnull().sum() > 0:
            na_cols[c] = test_x[c].value_counts().index[0]
    return na_cols


def target_encoding(y_train):
    y_train = [target_mapping[i] for i in y_train]
    return y_train


if __name__ == '__main__':
    train_x = read_data(config.c_xtrain)
    test_x = read_data(config.c_xtest)

    train_y = read_data(config.b_ytrain)
    train_y = target_encoding(train_y)

    impute_data = most_frequent(train_x)
    train_x, test_x = label_encoding(train_x, test_x, impute_data)

    assert len(train_x.columns) == len(test_x.columns)

    print('#### Writing Pickle 04: Imputation ####')
    write_data(config.d_xtrain, train_x)
    write_data(config.d_xtest, test_x)
    write_data(config.d_ytrain, train_y)
