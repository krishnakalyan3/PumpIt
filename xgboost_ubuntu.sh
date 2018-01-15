#!/usr/bin/env bash

git clone --recursive https://github.com/dmlc/xgboost
cd xgboost; make -j4
cd python-package; sudo python3 setup.py install
