import pandas as pd

data = pd.read_csv("dataset.csv")
print("\nMissing values in the csv file: ")
print(data.isnull().sum())

print("\nMissing values in LotFrontage: \n")
print(data['LotFrontage'].isnull())
print("\nupdated LotFrontage values(changed to '-1' for LotFrontage instead of NA): \n")
data['LotFrontage'].fillna('-1',inplace = True)
print(data['LotFrontage'])

print("\nMissing values in Alley: \n")
print(data['Alley'].isnull())
print("\nupdated Alley values(changed to 'empty' for Alley instead of NA): \n")
data['Alley'].fillna('empty_Alley',inplace = True)
print(data['Alley'])

print("\n",data[data['BsmtQual'].isnull()])

print("\nupdated BsmtQual values(changed to 'empty' for BsmtQual instead of NA): \n")
data['BsmtQual'].fillna('empty_BsmtQual',inplace = True)
print(data[data['BsmtQual'].isnull()])

print("\n",data[data['BsmtQual'].isnull()])

print("\nupdated BsmtCond values(changed to 'empty' for BsmtCond instead of NA): \n")
data['BsmtCond'].fillna('empty_BsmtCond',inplace = True)
print(data[data['BsmtCond'].isnull()])

print("\n",data[data['BsmtExposure'].isnull()])

print("\nupdated BsmtExposure values(changed to 'empty' for BsmtExposure instead of NA): \n")
data['BsmtExposure'].fillna('empty_BsmtExposure',inplace = True)
print(data[data['BsmtExposure'].isnull()])

print("\n",data[data['BsmtFinType1'].isnull()])

print("\nupdated BsmtFinType1 values(changed to 'empty' for BsmtFinType1 instead of NA): \n")
data['BsmtFinType1'].fillna('empty_BsmtFinType1',inplace = True)
print(data[data['BsmtFinType1'].isnull()])

print("\n",data[data['BsmtFinType2'].isnull()])

print("\nupdated BsmtFinType2 values(changed to 'empty' for BsmtFinType2 instead of NA): \n")
data['BsmtFinType2'].fillna('empty_BsmtFinType2',inplace = True)
print(data[data['BsmtFinType2'].isnull()])

print("\n\nUpdated csv file: \n")
print(data.isnull().sum())
