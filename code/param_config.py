#!/usr/bin/env python3


class Param:

    def __init__(self):
        self.set_seed = 123
        self.verbose = 100
        self.data_folder = '/Users/krishnakalyan3/Educational/PumpIt/data/'
        #self.data_folder = '/home/ubuntu/PumpIt/data/'
        self.sample = self.data_folder + 'original/' + 'SubmissionFormat.csv'
        self.train_file = self.data_folder + 'original/' + 'train_set_values.csv'
        self.test_file = self.data_folder + 'original/' + 'test_set_values.csv'
        self.target_file = self.data_folder + 'original/' + 'train_set_labels.csv'
        self.pickle_dir = self.data_folder + 'pickle_files/'
        self.submit_dir = self.data_folder + 'submit/'
        self.grid_report_rf = self.data_folder + 'grid_report/' + 'grid_rf.pkl'
        self.grid_report_xg = self.data_folder + 'grid_report/' + 'grid_xg.pkl'

        self.no_clusters = 10
        self.pca_components = 3
        self.train_val_split_pct = 0.20
        self.pkl_name = 'exp1_'

        # 01 missing
        self.a_xtrain = self.pickle_dir + self.pkl_name + '01_' + 'xtrain_' + 'missing.pkl'
        self.a_xtest = self.pickle_dir + self.pkl_name + '01_' + 'xtest_' + 'missing.pkl'

        # 02 date
        self.b_xtrain = self.pickle_dir + self.pkl_name + '02_' + 'xtrain_' + 'date.pkl'
        self.b_xtest = self.pickle_dir + self.pkl_name + '02_' + 'xtest_' + 'date.pkl'
        self.b_ytrain = self.pickle_dir + self.pkl_name + '02_' + 'ytrain_' + 'date.pkl'

        # 03 kmeans
        self.c_xtrain = self.pickle_dir + self.pkl_name + '03_' + 'xtrain_' + 'kmeans.pkl'
        self.c_xtest = self.pickle_dir + self.pkl_name + '03_' + 'xtest_' + 'kmeans.pkl'

        # 04 label encoding
        self.d_xtrain = self.pickle_dir + self.pkl_name + '04_' + 'xtrain_' + 'le.pkl'
        self.d_xtest = self.pickle_dir + self.pkl_name + '04_' + 'xtest_' + 'le.pkl'
        self.d_ytrain = self.pickle_dir + self.pkl_name + '04_' + 'ytrain_' + 'le.pkl'

        # 05 imbalance by over sampling
        self.e_xtrain = self.pickle_dir + self.pkl_name + '05_' + 'xtrain_' + 'imbal.pkl'
        self.e_ytrain = self.pickle_dir + self.pkl_name + '05_' + 'ytrain_' + 'imbal.pkl'

        # 09 split
        self.f_xtrain = self.pickle_dir + self.pkl_name + '09_' + 'xtrain_' + 'split.pkl'
        self.f_ytrain = self.pickle_dir + self.pkl_name + '09_' + 'ytrain_' + 'split.pkl'
        self.f_xval = self.pickle_dir + self.pkl_name + '09_' + 'xval_' + 'split.pkl'
        self.f_yval = self.pickle_dir + self.pkl_name + '09_' + 'yval_' + 'split.pkl'

        # Extra Feat #
        # 01 PCA
        self.pca_xtrain = self.pickle_dir + self.pkl_name + '01_' + 'xtrain_' + 'pca.pkl'
        self.pca_xtest = self.pickle_dir + self.pkl_name + '01_' + 'xtest_' + 'pca.pkl'

        # self.imputation_stratergy = 'most_frequent'

# TODO
# Number of days since data recorded
# Construction Year
# Bayesean optimization SVM
# Auto Encoder Feat Cat
# Imbalance Learn
# Check default values of RF and XGBoost


# Finish Cat EDA

# Feat 2
    # PCA
    # TFIDF
    # 2 way / 3 way interactions

# Algorithms
    # XGBoost
    # Neural Network

# Predict on test set and train

# Over sampling
# make all plots
# random forest
# interactions
# PCA
# clipping outlier
# See if dropping outliers help
# classification tasks, plot the data with points colored according to their labels
    # Done
    # numerical variables, use box plot and scatter plot


config = Param()
