import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df = pd.read_excel('Dataset for Data Analytics (2).xlsx')
# Display the first 5 rows
print('First 5 rows:')
print(df.head())
# Display the number of rows and columns
print('\nDataset Shape:')
print(df.shape)
# Display column Names
print('\nColumn Names:')
print(df.columns)
# Display basic statistics
print('\nBasic Statistics:')
print(df.describe())
# Baxplot to identify outliers in TotalPrice
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['TotalPrice'])
plt.title('Boxplot of TotalPrice')
plt.show()
# Check for missing values 
print ('\nMissing Values:')
print (df.isnull().sum())
# Check for duplicate rows 
print ('\nDuplicate Rows:')
print (df.duplicated().sum())
# Correlation analysis
print('\nCorrelation Matrix:')
print(df[['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']].corr())
# Summary of key observations
print('\nKey Observations:')
print('This analysis of 1,200 e-commerce orders shows an average order value of ₦1,053.97,')
print('with most orders falling between ₦410.52 and ₦1,578.48. A small number of high-value')
print('orders (up to ₦3,456.40) stand out as outliers. The data has no duplicate records,')
print('though 309 orders are missing a coupon code, likely customers who simply did not use one.')
print('TotalPrice is most strongly influenced by UnitPrice (0.72) and Quantity (0.62), while')
print('price does not appear to affect how many items customers buy (correlation of only 0.01')
print('between UnitPrice and Quantity).')