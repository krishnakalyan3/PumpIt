#!/usr/bin/env python3

import pickle
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from mapping import inverse_mapping
import pandas as pd
from param_config import config


def write_data(PATH, data):
    with open(PATH, 'wb') as fp:
        pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)


def read_data(PATH):
    with open(PATH, 'rb') as fp:
        data = pickle.load(fp)
    return data


def metrics(y, y_hat):
    accuracy = accuracy_score(y, y_hat)
    f1 = f1_score(y, y_hat, average='weighted')
    print('{} F1'. format(f1))
    print('{} Accuracy'.format(accuracy))
    return f1


def submit(yhat, file_name):
    submit = pd.read_csv(config.sample)
    submit['status_group'] = [inverse_mapping[i] for i in yhat]
    submit.to_csv(config.submit_dir + file_name, index=False)
    print('file created')


def aug_submit(clf, train_x, train_y):
    test_x = read_data(config.d_xtest)

    # Train Model
    clf.fit(train_x, train_y)

    # Predict on Test
    yhat_test = clf.predict(test_x)

    # Combine Data
    all_x = train_x.append(test_x)
    all_y = train_y + yhat_test.tolist()

    # Fit again
    clf.fit(all_x, all_y)

    # Predict on Test
    yhat_test = clf.predict(test_x)

    return yhat_test