from sklearn.model_selection import train_test_split
import pandas as pd


fw = pd.read_csv('data_source/log2.csv')
# split the data into train and test set
train, test = train_test_split(fw, test_size=0.30, random_state=0,stratify=fw['Action'])

# save the data
# train.to_csv('data_source/train.csv',index=False)
# test.to_csv('data_source/test.csv',index=False)

# test = pd.read_csv('data_source/test.csv')
# train = pd.read_csv('data_source/train.csv')
print('hello')
