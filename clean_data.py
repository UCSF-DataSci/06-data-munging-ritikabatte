import pandas as pd

df = pd.read_csv('/Users/ritikabatte02/06-data-munging-ritikabatte/messy_population_data.csv')

# print(df.head())
# print(df.describe())
# print(df.isnull().sum())
# print(df.duplicated().sum())    
# print(df.dtypes)
# print(df.info())
# print(df.value_counts())


# exclude rows that contain negative values
df = df[df['population'] > 0]
# print(df.describe())

# remove gender entry of "3" from the dataset
df = df[df['gender'] != 3]  
# print(df.describe())

# remove rows with years later than 2023
df = df[df['year'] <= 2023]

# make the year column a string
df['year'] = df['year'].astype(int)

# remove _typo from the end of entres that have them in income_groups column
df['income_groups'] = df['income_groups'].str.replace('_typo', '')
# print(df['income_groups'].value_counts())

#  remove rows where the population is 1.5 times the IQR less than Q1 or 1.5 times the IQR greater than Q3
Q1 = df['population'].quantile(0.25)
Q3 = df['population'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['population'] > (Q1 - 1.5 * IQR)) & (df['population'] < (Q3 + 1.5 * IQR))]
# # print(df.describe())

# exclude rows that contain NA values 
df = df.dropna()
# print(df.isnull().sum())

# exclude rows that contain duplicate values
df = df.drop_duplicates()
# print(df.duplicated().sum())

# With all the cleaning done, save the cleaned data to a new CSV file
# df.to_csv('/Users/ritikabatte02/06-data-munging-ritikabatte/cleaned_population_data.csv', index=False)  

print(df.head())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)
print(df.info())
print(df.value_counts())


