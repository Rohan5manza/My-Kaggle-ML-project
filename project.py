
#Importing Modules

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
import plotly.express as px
import plotly.graph_objs as go

import numpy as np
import pandas as pd
%matplotlib inline
from IPython.display import clear_output
%tensorflow_version 2.x 
from six.moves import urllib



import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow import feature_column as fc

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import sklearn.metrics as met
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn import model_selection
from sklearn.cluster import KMeans


import seaborn as Sb

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
/kaggle/input/spaceship-titanic/sample_submission.csv
/kaggle/input/spaceship-titanic/train.csv
/kaggle/input/spaceship-titanic/test.csv
UsageError: Line magic function `%tensorflow_version` not found.
 
path= Path('../input/spaceship-titanic')
os.listdir('path')
target_col='Transported'
# dataset sample

sample=pd.read_csv("../input/spaceship-titanic/sample_submission.csv")
sample.head().style.background_gradient(cmap="Pastel2")
#datasets

d_train=pd.read_csv("../input/spaceship-titanic/train.csv")
d_test=pd.read_csv("../input/spaceship-titanic/test.csv")
d_train.shape,d_test.shape,sample.shape
d_train.describe()
display(d_train.info())
display(d_test.info())
# Tabulating and displaying datasets


d_train.head().style.background_gradient(cmap="Pastel2")
d_test.head().style.background_gradient(cmap="Pastel1")
d_train[target_col].value_counts()
import pandas_profiling as pp
pp.ProfileReport(d_train)
pp.ProfileReport(d_test)
from sklearn.preprocessing import Min
# There are a lot of missing values from training and testing datasets so let's sort them out first.apply missing value imputation to them
# Tables columns like Age, cabin,etc, have missing info. Replace categorical missing data with most frequent values, and replace numerical values with average of all values of that feature

train.isnull().sum()
test.isnull().sum()

categorical_impstrat= ["mode", "unknown","KNN"][1]
numerical_imptrat=["mean","median","KNN"][2]


cols_with_missing_train = [col for col in train_data.columns if train_data[col].isnull().any()]
cols_with_missing_test = [col for col in test_data.columns if test_data[col].isnull().any()]
print('train columns with missing data:', cols_with_missing_train)
print('test columns with missing data:', cols_with_missing_test)

for col in cols_with_missing_train:
    most_freq = d_train[col].value_counts().index[0]
    train_data[col] = d_train[col].fillna(most_freq)
    test_data[col] = d_test[col].fillna(most_freq)


    
    
CATEGORICAL_COLUMNS = ['HomePlan', 'CryoSleep', 'Cabin', 'Destination', 'VIP',
                       'Name', 'Transported']
NUMERIC_COLUMNS = ['Passenger','Age', 'RoomService','FoodCourt','ShoppingMall','Spa','VRdeck']

feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
  vocabulary = dftrain[feature_name].unique()  # gets a list of all unique values from given feature column
  feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
  feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

print(feature_columns)
#Model (Tensorflow and Keras to use linear regression)

from keras.models import Sequential
from keras.layers import Dense,Activation,Dropout
from keras.optimizers import SGD,Adam

y_train=d_train.pop('Transported')
y_eval=d_test.pop('Transported')

def make_input_fn(data_df,label_def,num_epochs=10,batch_size=32)
def input_function()

ds= tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
 if shuffle:
      ds = ds.shuffle(1000)  
    ds = ds.batch(batch_size).repeat(num_epochs)
    return ds 
  return input_function

train_input_fn = make_input_fn(d_train, y_train) 
eval_input_fn = make_input_fn(d_eval, y_eval, num_epochs=1, shuffle=False)
linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)

 
linear_est.train(train_input_fn) 
result = linear_est.evaluate(eval_input_fn)  

clear_output() 
print(result['accuracy'])  
#this predicts the probability of being transported to another dimension
pred_dicts = list(linear_est.predict(eval_input_fn))
probs = pd.Series([pred['probabilities'][1] for pred in pred_dicts])

probs.plot(kind='hist', bins=20, title='predicted probabilities')
