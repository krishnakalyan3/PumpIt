#!/usr/bin/env python3

import sys
sys.path.append("../")

from param_config import config
from utils import read_data
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Merge, Reshape, Dropout
from keras.layers.embeddings import Embedding
from keras.utils.np_utils import to_categorical
from mapping import data_card

np.random.seed(config.set_seed)


def embedding_network(input_shape, embed_shape):
    model = Sequential()
    model.add(Embedding(input_shape, embed_shape, input_length=1))
    model.add(Reshape(target_shape=(embed_shape,)))
    return model


def model_all():
    model = embedding_network(cardinality, embed)
    model.append(model)

    model = Sequential()
    model.add(Merge(models, mode='concat'))
    model.add(Dense(500))
    model.add(Activation('relu'))
    model.add(Dropout(0.05))
    model.add(Dense(10))
    model.add(Activation('relu'))
    model.add(Dropout(.15))
    model.add(Dense(3))
    model.add(Activation('softmax'))
    model.compile('rmsprop', 'categorical_crossentropy')
    return model


def embedding(x_train, y_train):
    cat_var = data_card.keys()
    master_model = model_all(x_train)
    master_model.summary()

    X = [x_train[i].values for i in list(cat_var)]
    y = to_categorical(np.array(y_train.values))

    master_model.fit(X, y, batch_size=256, verbose=1, epochs=2)
    exit()

    print(x_train[cat_var].values)
    exit()

    exit()


    model = embedding_network(cardinality, 50)
    #model.fit(x_train[cc], epochs=20, validation_split=0.3, batch_size=64)
    return model

if __name__ == '__main__':
    train_x = read_data(config.d_xtrain)
    train_y = read_data(config.d_ytrain)

    cols_needed = ['date_recorded', 'amount_tsh']
    train_x = train_x[cols_needed]
    print(train_x.head())
    print()

