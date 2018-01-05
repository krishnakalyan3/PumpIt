#!/usr/bin/env python3


class Param:

    def __init__(self):
        self.data_folder = '/Users/krishnakalyan3/Educational/PumpIt/data/'
        self.train_file = self.data_folder + 'original/' + 'train_set_values.csv'
        self.test_file = self.data_folder + 'original/' + 'test_set_values.csv'
        self.target_file = self.data_folder + 'original/' + 'train_set_labels.csv'
        self.pickle_dir = self.data_folder + 'pickle_files/'
        self.imputation_stratergy = 'most_frequent'
        self.pkl_name = 'exp1_'


        # 01 missing
        self.a_xtrain = self.pickle_dir + self.pkl_name + '01_' + 'xtrain_' + 'missing.pkl'
        self.a_xtest = self.pickle_dir + self.pkl_name + '01_' + 'xtest_' + 'missing.pkl'
        self.a_ytest = self.pickle_dir + self.pkl_name + '01_' + 'ytrain_' + 'missing.pkl'

        # 02 impute
        self.b_xtrain = self.pickle_dir + self.pkl_name + '02_' + 'xtrain_' + 'impute.pkl'
        self.b_xtest = self.pickle_dir + self.pkl_name + '02_' + 'xtest_' + 'impute.pkl'


config = Param()