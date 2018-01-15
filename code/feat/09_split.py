#!/usr/bin/env python3

import sys
sys.path.append("../")
from param_config import config
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import ADASYN, SMOTE, RandomOverSampler
from utils import read_data
from utils import write_data
import numpy as np
np.random.seed(config.set_seed)


def join_split(X, y):
    x_train, x_val, y_train, y_val = train_test_split(X, y, stratify=y, test_size=config.train_val_split_pct)
    return x_train, y_train, x_val, y_val


# Try imbalance learn

if __name__ == '__main__':
    train_x = read_data(config.e_xtrain)
    train_y = read_data(config.e_ytrain)

    # split data into train and validation
    # 20 percent stratified
    x_train, y_train, x_val, y_val = join_split(train_x, train_y)

    print('#### Writing Pickle 09: Split ####')
    write_data(config.f_xtrain, x_train)
    write_data(config.f_ytrain, y_train)
    write_data(config.f_xval, x_val)
    write_data(config.f_yval, y_val)
