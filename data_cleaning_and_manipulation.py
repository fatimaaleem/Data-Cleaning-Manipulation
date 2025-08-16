print("Data cleaning is the process of identifying and correcting errors, inconsistencies, and missing values in a dataset. Its purpose is to ensure the data is accurate, reliable, and suitable for analysis. Common issues include incorrect data types, duplicate entries, outliers, and structural errors.")
print("\nData manipulation involves transforming and restructuring data to make it ready for analysis. This can include filtering, sorting, aggregating, merging, and pivoting data. It's about shaping the data into a format that allows for meaningful insights and effective model building.")
print("\nBoth data cleaning and manipulation are crucial because they directly impact the quality of the data. High-quality data leads to more reliable analysis, more accurate models, and ultimately, better decision-making. Poorly cleaned or manipulated data can lead to misleading results and flawed conclusions.")
print("1. Handling Missing Data:")
print("   Missing data occurs when no data value is stored for a variable in an observation. Common strategies include:")
print("   - Deletion: Removing rows or columns with missing values. This is simple but can lead to loss of valuable data.")
print("   - Imputation: Replacing missing values with estimated values. Common methods include mean, median, mode imputation, or using more sophisticated techniques like K-Nearest Neighbors or regression imputation.")
print(" . Dealing with Outliers:")
print("   Outliers are data points significantly different from other observations. They can distort statistical analyses. Methods for identification and handling include:")
print("   - Z-scores: Measuring how many standard deviations a data point is from the mean. A common threshold is a z-score greater than 3 or less than -3.")
print("   - Interquartile Range (IQR): Calculating the difference between the third and first quartiles (Q3 - Q1). Outliers are often considered points below Q1 - 1.5*IQR or above Q3 + 1.5*IQR.")
print("   - Visualization Techniques: Box plots, scatter plots, and histograms can visually reveal outliers.")
print("   - Handling: Outliers can be removed, transformed (e.g., log transformation), or capped/floored at a certain value.")
print("\n3. Data Type Conversion:")
print("   Ensuring variables are in the correct data type (e.g., integer, float, string, datetime) is crucial for proper analysis and calculations. Incorrect data types can lead to errors or incorrect results.")
print("\n4. Data Normalization:")
print("   Scaling numerical features to a standard range (e.g., 0 to 1 or a mean of 0 and standard deviation of 1). This is important for algorithms sensitive to the scale of input features, such as gradient descent-based methods and distance-based algorithms like K-Nearest Neighbors and Support Vector Machines.")
print("   - Min-Max Scaling: Scales data to a fixed range, usually [0, 1].")
print("   - Standardization (Z-score normalization): Scales data to have a mean of 0 and a standard deviation of 1.")
print("\n5. Data Transformation:")
print("   Applying mathematical functions to a feature to change its distribution or relationship with other variables. This is often done to address skewness, stabilize variance, or meet the assumptions of certain statistical models.")
print("   - Log Transformation: Useful for right-skewed data.")
print("   - Square Root Transformation: Can also help with right-skewed data.")
print("   - Reciprocal Transformation: Can be used for skewed data.")
print("   - Power Transformations (e.g., Box-Cox): A family of transformations that can make data more normally distributed.")
# examples
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'],
    'Age': [24, 35, np.nan, 42, 29, 55, 31, 27, 65, 38],
    'Salary': [50000, 60000, 70000, np.nan, 55000, 150000, 62000, 58000, 200000, 61000],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Experience': [2, 8, 5, 15, 3, 25, 6, 4, 35, 10],
    'Score': [85.5, 90.1, 78.9, 92.0, 88.7, 65.0, 81.3, 89.9, 50.0, 76.5]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
# Although we already have a DataFrame, this is how you would typically read from a CSV file
# Assuming 'sample_data.csv' exists with similar data
# try:
#     df_csv = pd.read_csv('sample_data.csv')
#     print("\nDataFrame read from CSV:")
#     display(df_csv.head())
# except FileNotFoundError:
#     print("\n'sample_data.csv' not found. Skipping CSV read example.")

# For demonstration purposes, we'll just print a message about reading from CSV
print("To read data from a CSV file, you would typically use: pd.read_csv('your_file.csv')")
# Handling missing values

# Check for missing values
print("\nMissing values before handling:")
print(df.isnull().sum())

# Option 1: Drop rows with any missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)

# Option 2: Fill missing values
# Fill missing Age with the mean age
mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True)

# Fill missing Salary with the median salary
median_salary = df['Salary'].median()
df['Salary'].fillna(median_salary, inplace=True)

print("\nDataFrame after filling missing values:")
print(df)
# Identifying and handling outliers

# Example: Identify potential outliers in 'Salary' using IQR
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]
print("\nPotential outliers in Salary using IQR:")
print(outliers)

# Example: Handling outliers by filtering
df_filtered_outliers = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]
print("\nDataFrame after filtering out Salary outliers using IQR:")
print(df_filtered_outliers)

# Example: Identify potential outliers in 'Experience' based on a simple condition
experience_outliers = df[df['Experience'] > 20]
print("\nPotential outliers in Experience (Experience > 20):")
print(experience_outliers)
# Data type conversion

print("\nData types before conversion:")
print(df.dtypes)

# Convert 'Experience' column to float
df['Experience'] = df['Experience'].astype(float)

# Convert 'Score' column to integer (this will truncate decimals)
# Be cautious with this conversion as it loses precision
# df['Score'] = df['Score'].astype(int) # Uncomment to see the effect

print("\nData types after converting 'Experience' to float:")
print(df.dtypes)
# Data transformation

# Example: Create a new column 'Salary_USD_per_Experience_Year'
df['Salary_per_Experience'] = df['Salary'] / (df['Experience'] + 1) # Add 1 to avoid division by zero

print("\nDataFrame after adding 'Salary_per_Experience' column:")
print(df)

# Example: Apply a log transformation to the 'Salary' column (useful for skewed data)
# Add a small constant to avoid log(0) if 0 values exist
df['Salary_Log'] = np.log(df['Salary'] + 1)

print("\nDataFrame after adding 'Salary_Log' column:")
print(df)
# Merging/Joining datasets

# Create another sample DataFrame with additional information
data_city = {
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Country': ['USA', 'UK', 'France', 'Japan', 'Australia']
}
df_city = pd.DataFrame(data_city)

print("\nSecond DataFrame (City Information):")
print(df_city)

# Merge the two DataFrames on the 'City' column
df_merged = pd.merge(df, df_city, on='City', how='left')

print("\nMerged DataFrame:")
print(df_merged)
# Save the DataFrame to a CSV file
df.to_csv('cleaned_data.csv', index=False)

print("DataFrame saved to 'cleaned_data.csv'")