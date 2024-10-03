import pandas as pd
import matplotlib.pyplot as plt

data_file = 'sales_data.csv'
data = pd.read_csv(data_file)

print("Missing values before cleaning:")
print(data.isnull().sum())

data.dropna(inplace=True)

print("Missing values after cleaning:")
print(data.isnull().sum())

print("Basic statistics of the dataset:")
print(data.describe())

print("Data types and first few rows:")
print(data.dtypes)
print(data.head())

data['Date'] = pd.to_datetime(data['Date'])

plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Sales'], marker='o', linestyle='-')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()

total_sales = data['Sales'].sum()
print(f'Total Sales: {total_sales}')

monthly_sales = data.resample('M', on='Date').sum()

plt.figure(figsize=(10, 5))
plt.bar(monthly_sales.index, monthly_sales['Sales'], color='skyblue')
plt.title('Total Sales Per Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
