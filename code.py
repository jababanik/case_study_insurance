# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:47:37 2019

@author: TCI
"""

import pandas as pd
dataset = pd.read_excel("case_study_data.xlsx")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 20].values

from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
labelencoder_X.fit_transform(X)