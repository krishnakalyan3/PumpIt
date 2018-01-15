#!/usr/bin/env python3

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

UTILS = '../'
import sys
sys.path.append(UTILS)
# Custom imports
from utils import read_data, write_data, metrics, submit
from param_config import config


param_grid = {"criterion": ["gini", "entropy"],

              "min_samples_split": [2, 3, 4, 5, 6],
              "min_samples_leaf": np.arange(1, 10, 1),
              "min_weight_fraction_leaf": np.arange(0.1, 0.4, 0.1),

              "max_depth": np.arange(1, 28, 1),
              "max_features": ['auto', 'sqrt', 'log2'],
              "max_leaf_nodes": np.arange(2, 10, 2),

              "n_estimators": [50, 100, 400, 700, 1000],

              # min_impurity_split
              # min_impurity_decrease
              }


def grid_model(params, X, y, cv=5):
    rf = RandomForestClassifier(max_features='auto', oob_score=False, class_weight='balanced',
                                random_state=config.set_seed, n_jobs=-1, verbose=0)
    clf = GridSearchCV(estimator=rf, param_grid=params, scoring='accuracy', cv=cv, n_jobs=-1)
    clf.fit(X, y)

    print('#### Best Params')
    print(clf.best_params_)
    print('#### Best Score')
    print(clf.best_score_)
    return clf.grid_scores_


if __name__ == '__main__':
    # Train Data
    train_x = read_data(config.d_xtrain)
    train_y = read_data(config.d_ytrain)

    # Test Data
    test_x = read_data(config.d_xtest)
    report = grid_model(param_grid, train_x, train_y, cv=5)

    write_data(config.grid_report_rf, report)
