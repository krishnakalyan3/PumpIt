#!/usr/bin/env python3
import numpy as np

TOTAL_RUNS = 5000
param_grid = {"C": np.logspace(-4, 6, 5000),
              "gamma": np.logspace(-5, 6, 5000)}

