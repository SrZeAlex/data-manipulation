import pandas as pd
import csv

dataset = pd.read_csv('bike_usage_2012.csv')
#dataset 

print('shape: ', dataset.shape)

print('\ncolumns: ', dataset.columns)

print('\ndata types: ', dataset.dtypes)

print('\nMissing values:\n', dataset.isnull().sum())

print('\n Duplicated rows: ', dataset.duplicated().sum())

print('\nSummary statistics:\n', dataset.describe())

print('\nTop 5 rows:\n', dataset.head())