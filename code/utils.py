#!/usr/bin/env python3

import pickle


def write_data(PATH, data):
    with open(PATH, 'wb') as fp:
        pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)


def read_data(PATH):
    with open(PATH, 'rb') as fp:
        data = pickle.load(fp)
    return data
