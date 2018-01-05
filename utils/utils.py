#!/usr/bin/env python3

from sklearn.preprocessing import LabelEncoder
import pandas as pd



class MultiColumnLabelEncoder:
    def __init__(self,columns = None):
        self.columns = columns # array of column names to encode

    def fit(self,X,y=None):
        return self # not relevant here

    def transform(self,X):
        '''
        Transforms columns of X specified in self.columns using
        LabelEncoder(). If no columns specified, transforms all
        columns in X.
        '''
        output = X.copy()
        if self.columns is not None:
            for col in self.columns:
                output[col] = LabelEncoder().fit_transform(output[col])
        else:
            for colname,col in output.iteritems():
                output[colname] = LabelEncoder().fit_transform(col)
        return output

    def fit_transform(self,X,y=None):
        return self.fit(X,y).transform(X)


def combine_split(train, test, rem_col=[]):
    rem_col = ['id', 'price_doc']
    x_cols = [col for col in train.columns if col not in rem_col]

    train_dim = train.shape
    test_dim = test.shape
    print('train shape {}, test shape {} '.format(train_dim, test_dim))
    df_train = train[x_cols]
    df_test = test[x_cols]

    df = pd.concat([df_train, df_test], axis=0)

    objects_col = []
    for c in df.columns:
        if df[c].dtype == 'object':
            objects_col.append(c)
            lbl = LabelEncoder()
            lbl.fit(list(df[c].values))
            df[c] = lbl.transform(list(df[c].values))
    print('All object cols {}'.format(objects_col))

    dtr = df[0:train_dim[0]]
    dtr = pd.concat([dtr, train[rem_col]], axis=1)

    dtt = df[train_dim[0]:train_dim[0] + test_dim[0]]
    dtt = pd.concat([dtt, test[rem_col[0]]], axis=1)

    return dtr, dtt


