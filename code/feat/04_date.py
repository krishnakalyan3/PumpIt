#!/usr/bin/env python3

import sys
sys.path.append("../")
from param_config import config
from utils import read_data
from utils import write_data
import numpy as np
from datetime import datetime
import pandas as pd
np.random.seed(config.no_clusters)


def date_objects(df):
    date = pd.to_datetime(df['date_recorded'], format='%Y-%m-%d')
    year = date.apply(lambda x: x.year)
    month = date.apply(lambda x: x.month)
    day = date.apply(lambda x: x.day)
    return year, month, day


def date_process(x_train, x_test):
    y1, m1, d1 = date_objects(x_train)
    x_train['year'] = y1
    x_train['month'] = m1
    x_train['day'] = d1

    y2, m2, d2 = date_objects(x_test)
    x_train['year'] = y2
    x_train['month'] = m2
    x_train['day'] = d2

    return x_train, x_test


if __name__ == '__main__':
    train_x = read_data(config.c_xtrain)
    test_x = read_data(config.c_xtest)

    x_train, x_test = date_process(train_x, test_x)

    print('#### Writing Pickle 04 ####')
    write_data(config.d_xtrain, train_x)
    write_data(config.d_xtest, test_x)
