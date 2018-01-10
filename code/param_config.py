#!/usr/bin/env python3


class Param:

    def __init__(self):

        self.set_seed = 123
        self.data_folder = '/Users/krishnakalyan3/Educational/PumpIt/data/'
        self.train_file = self.data_folder + 'original/' + 'train_set_values.csv'
        self.test_file = self.data_folder + 'original/' + 'test_set_values.csv'
        self.target_file = self.data_folder + 'original/' + 'train_set_labels.csv'
        self.pickle_dir = self.data_folder + 'pickle_files/'
        self.no_clusters = 10
        self.pkl_name = 'exp1_'

        # 01 missing
        self.a_xtrain = self.pickle_dir + self.pkl_name + '01_' + 'xtrain_' + 'missing.pkl'
        self.a_xtest = self.pickle_dir + self.pkl_name + '01_' + 'xtest_' + 'missing.pkl'
        self.a_ytest = self.pickle_dir + self.pkl_name + '01_' + 'ytrain_' + 'missing.pkl'

        # 02 impute and encode
        self.b_xtrain = self.pickle_dir + self.pkl_name + '02_' + 'xtrain_' + 'impute.pkl'
        self.b_xtest = self.pickle_dir + self.pkl_name + '02_' + 'xtest_' + 'impute.pkl'
        self.b_ytest = self.pickle_dir + self.pkl_name + '02_' + 'ytrain_' + 'missing.pkl'

        # 03 kmeans
        self.c_xtrain = self.pickle_dir + self.pkl_name + '03_' + 'xtrain_' + 'kmeans.pkl'
        self.c_xtest = self.pickle_dir + self.pkl_name + '03_' + 'xtest_' + 'kmeans.pkl'

        # 04 data augmentation
        self.d_xtrain = self.pickle_dir + self.pkl_name + '04_' + 'xtrain_' + 'date.pkl'
        self.d_xtest = self.pickle_dir + self.pkl_name + '04_' + 'xtest_' + 'date.pkl'



        # self.imputation_stratergy = 'most_frequent'

# TODO
# Finish Cat EDA

# Algorithms
    # XGBoost
    # Neural Network

# Predict on test set and train

# Over sampling
# make all plots
# random forest
# interactions
# PCA
# LSA
# TF-IDF
# See if dropping outliers help
# numerical variables, use box plot and scatter plot
# classification tasks, plot the data with points colored according to their labels

config = Param()
