#!/usr/bin/env python3

import numpy as np
from xgboost.sklearn import XGBClassifier
from sklearn.grid_search import GridSearchCV, RandomizedSearchCV

UTILS = '../'
import sys
sys.path.append(UTILS)
# Custom imports
from utils import read_data, write_data, metrics, submit
from param_config import config

# Early Stopping

params_grid = {
    'max_depth': [1, 3, 6, 9],
    'subsample': [0.4, 0.6, 0.8, 1.0],
    'n_estimators': [5, 10, 25, 50, 100],
    'min_child_weight': [1, 3, 5],
    'learning_rate': [0.1, 0.01],
    'colsample_bytree': [0.5, 0.7, 0.9]
}

params_fixed = {
    'objective': 'multi:softmax'
}


def grid_model(X, y, cv=5):
    clf = GridSearchCV(
        estimator=XGBClassifier(**params_fixed, seed=config.set_seed),
        param_grid=params_grid,
        verbose=0,
        cv=cv,
        scoring='accuracy'
    )

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
    report = grid_model(train_x, train_y, cv=5)

    write_data(config.grid_report_xg, report)
