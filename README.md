# Initial Data Overview: 
- Dataset: messy_population_data.csv
- Total Rows: 125718
- Total Columns: 5
     Column        | Non-Null | Count    | Dtype  
--------------------------------------------- 
 0|  income_groups | 119412   | non-null | object 
 1|  age           | 119495   | non-null | float64
 2|  gender        | 119811   | non-null | float64
 3|  year          | 119516   | non-null | float64
 4|  population    | 119378   | non-null | float64

# Part 1: Identifying Data Issues: 
- Columns affected: income_groups (categorical), gender (categorical), age (numeric), year (categorical), population (numeric)
- There's alot missing values in all the columns so it can skew the results
- There are 2950 duplicated rows in the dataset and it affects every column 
- The gender column has 1 and 3 as it's category which is confusing because most studies only have gender as 2 categories
- Year column should be a integer not a float because 1952 is very different than 1952.0
- The income_groups column has _typo for one of the categories which is weird to read and not a good way of labeling since all the others don't have it. 
- Population column has a max value of 32 billion which isn't realistic


# Part 2: Cleaning the Data
- 1. Excluding rows that contain NA values 
```python
    df = df.dropna()
```
        - This removed all the missing values from the all the columns. Even though there weren't that many missing values compared to the entire dataset, removing them still would have made an impact to the results. 

- 2. Excluding rows that have duplicated columns 
```python 
    df = df.drop_duplicates()
```
        - This removed all the duplicated columns in the dataset so that it doesn't skew the results.

- 3. Removing gender entry of "3"
```python
    df = df[df['gender'] != 3]  
```
        - This takes out the "3" category for gender since there aren't 3 categories for gender so taking it out will give out better results. 

- 4. Removing rows with years later than 2023 and making year an integer 
```python
    df = df[df['year'] <= 2023]
    df['year'] = df['year'].astype(int)
```
        - This helps keep the data more accurate since its impossible to have data in the future

- 5. Removing _typo from the income_groups column 
```python
    df['income_groups'] = df['income_groups'].str.replace('_typo', '')
```
        - This takes out any of the typos in the column so there are more clear columns that are better named. 
- 6. Removing rows where the population is 1.5 times the IQR less than Q1 or 1.5 times the IQR greater than Q3
```python 
    Q1 = df['population'].quantile(0.25)
    Q3 = df['population'].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df['population'] > (Q1 - 1.5 * IQR)) & (df['population'] < (Q3 + 1.5 * IQR))] 
```
        - This makes population column more understandable and realistic to understand the data. I still think that it could be better. 

# Final Data Overview: 
- Dataset: cleaned_population_data.csv
- Total Rows: 39757
- Total Columns: 5
      Column       | Non-Null | Count    | Dtype  
---------------------------------------------------  
 0|  income_groups | 39757    | non-null | object 
 1|  age           | 39757    | non-null | float64
 2|  gender        | 39757    | non-null | float64
 3|  year          | 39757    | non-null | int64  
 4|  population    | 39757    | non-null | float64
- The cleaned dataset addresses key issues from the messy dataset by handling missing values, removing duplicated rows, and removing false entries like in gender, year, and income_groups. 
- One of the challeneges was the population entries because I wasn't sure how to handle the incorrect data entries since I don't know much about the dataset.
- I learned how to take a dirty dataset and make it clean without much about the data but see my intuiton to clean it to the best of my abilities. 
- Most of the future improvements are in the population column to make sure there is accuracy. I think it needs more steps to make that column better to use in modeling. 