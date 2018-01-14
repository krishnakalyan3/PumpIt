#!/usr/bin/env python3

import sys
sys.path.append("../")
from param_config import config
from utils import read_data
from utils import write_data
import numpy as np
import pandas as pd
np.random.seed(config.set_seed)


def date_objects(df):
    date = pd.to_datetime(df['date_recorded'], format='%Y-%m-%d')
    year = date.apply(lambda x: x.year)
    month = date.apply(lambda x: x.month)
    day = date.apply(lambda x: x.day)
    day_week = date.apply(lambda x: x.dayofweek)

    return year, month, day, day_week


def date_process(x_train, x_test):
    y1, m1, d1, dw1 = date_objects(x_train)
    x_train['year'] = y1
    x_train['month'] = m1
    x_train['day'] = d1
    x_train['day_week'] = dw1

    y2, m2, d2, dw2 = date_objects(x_test)
    x_test['year'] = y2
    x_test['month'] = m2
    x_test['day'] = d2
    x_test['day_week'] = dw2

    return x_train, x_test


def join_df(left, right, left_on, right_on=None, suffix='_y'):
    if right_on is None: right_on = left_on
    return left.merge(right, how='left', left_on=left_on, right_on=right_on,
                      suffixes=("", suffix))


def drop_cols(x_train, x_test):
    drop = ['status_group', 'id', 'quantity_group', 'recorded_by']
    for i in drop:
        if i == 'status_group':
            x_train = x_train.drop(i, axis=1)
        else:
            x_train = x_train.drop(i, axis=1)
            x_test = x_test.drop(i, axis=1)

    return x_train, x_test


if __name__ == '__main__':
    train_x = read_data(config.a_xtrain)
    train_y = pd.read_csv(config.target_file)
    test_x = read_data(config.a_xtest)

    # Date split year, month, day, day_of_week
    # merge X and y to a single df
    train_x, test_x = date_process(train_x, test_x)
    train_merge = join_df(train_x, train_y, 'id', 'id')
    train_y = train_merge['status_group']

    # Drop Columns
    train_x, test_x = drop_cols(train_merge, test_x)

    print('#### Writing Pickle 02: Date ####')
    write_data(config.b_xtrain, train_x)
    write_data(config.b_xtest, test_x)
    write_data(config.b_ytrain, train_y)
