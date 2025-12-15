# Databricks notebook source
data = dbutils.fs.ls("/Volumes/retailstore_analysis/retailschema/myvolume")

# COMMAND ----------

import pandas as pd
import numpy as np
# Convert to pandas DataFrame
retail_df = pd.DataFrame(data)

# Show first 5 rows
retail_df.head()

# COMMAND ----------

# Total sales per product
retail_df['TotalSales'] = retail_df['Quantity'] * retail_df['Price']
product_sales = retail_df.groupby('Product')[['TotalSales', 'Quantity']].sum().reset_index()
print("Product Sales:")
print(product_sales)

# Total sales per store
store_sales = retail_df.groupby('Store')['TotalSales'].sum().reset_index()
print("\nStore Sales:")
print(store_sales)

# Top 5 customers by spending
top_customers = retail_df.groupby('CustomerID')['TotalSales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Customers by Spending:")
print(top_customers)


# COMMAND ----------

import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Total Sales by Product
plt.figure(figsize=(8,5))
sns.barplot(x='Product', y='TotalSales', data=product_sales, palette='viridis')
plt.title('Total Sales by Product')
plt.ylabel('Total Sales')
plt.show()

# 2️⃣ Total Sales by Store
plt.figure(figsize=(6,4))
sns.barplot(x='Store', y='TotalSales', data=store_sales, palette='magma')
plt.title('Total Sales by Store')
plt.ylabel('Total Sales')
plt.show()

# 3️⃣ Sales Trend over Time
sales_trend = retail_df.groupby('Date')['TotalSales'].sum().reset_index()
plt.figure(figsize=(10,4))
sns.lineplot(x='Date', y='TotalSales', data=sales_trend, marker='o')
plt.title('Daily Sales Trend')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


# COMMAND ----------

# Total sales per transaction (already done before)
retail_df['TotalSales'] = retail_df['Quantity'] * retail_df['Price']

# Extract month and day from Date for trend analysis
retail_df['Month'] = retail_df['Date'].dt.month
retail_df['DayOfWeek'] = retail_df['Date'].dt.day_name()

# COMMAND ----------

# Top 5 products by total sales
top_products = retail_df.groupby('Product')['TotalSales'].sum().sort_values(ascending=False).head(5)
print("Top 5 Products by Sales:\n", top_products)

# Average quantity sold per product
avg_quantity = retail_df.groupby('Product')['Quantity'].mean().sort_values(ascending=False)
print("\nAverage Quantity Sold per Product:\n", avg_quantity)


# COMMAND ----------

# Correlation between Quantity, Price, and TotalSales
correlation = retail_df[['Quantity', 'Price', 'TotalSales']].corr()
print("Correlation:\n", correlation)

# Heatmap of correlations
plt.figure(figsize=(6,5))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()


# COMMAND ----------

import matplotlib.pyplot as plt
import seaborn as sns

# Prepare data
product_sales = retail_df.groupby('Product')['TotalSales'].sum()
store_sales = retail_df.groupby('Store')['TotalSales'].sum()
monthly_sales = retail_df.groupby('Month')['TotalSales'].sum()
top_customers = retail_df.groupby('CustomerID')['TotalSales'].sum().sort_values(ascending=False).head(5)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(14,10))

# 1️⃣ Pie chart: Product Sales Distribution
axes[0,0].pie(product_sales.values, labels=product_sales.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
axes[0,0].set_title('Product Sales Distribution')

# 2️⃣ Bar chart: Store Sales
sns.barplot(x=store_sales.index, y=store_sales.values, palette='magma', ax=axes[0,1])
axes[0,1].set_title('Total Sales by Store')
axes[0,1].set_ylabel('Total Sales')

# 3️⃣ Line chart: Monthly Sales Trend
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o', ax=axes[1,0])
axes[1,0].set_title('Monthly Sales Trend')
axes[1,0].set_xlabel('Month')
axes[1,0].set_ylabel('Total Sales')

# 4️⃣ Horizontal bar chart: Top 5 Customers
sns.barplot(x=top_customers.values, y=top_customers.index, palette='cividis', ax=axes[1,1])
axes[1,1].set_title('Top 5 Customers by Spending')
axes[1,1].set_xlabel('Total Spending')
axes[1,1].set_ylabel('CustomerID')

plt.tight_layout()
plt.show()

# COMMAND ----------

import matplotlib.pyplot as plt

# Create a bubble chart
plt.figure(figsize=(10,6))

# X-axis: Price, Y-axis: TotalSales, Bubble size: Quantity
plt.scatter(
    x=retail_df['Price'],
    y=retail_df['TotalSales'],
    s=retail_df['Quantity']*50,  # bubble size (scaled for visibility)
    alpha=0.6,
    c=retail_df['Quantity'],      # color represents Quantity
    cmap='viridis'
)

plt.colorbar(label='Quantity')  # color legend
plt.xlabel('Price')
plt.ylabel('Total Sales')
plt.title('Bubble Chart: Price vs TotalSales (Bubble size = Quantity)')
plt.show()

# COMMAND ----------

import matplotlib.pyplot as plt
import pandas as pd

# Pivot table: Products as columns, Stores as rows
store_product = retail_df.pivot_table(index='Store', columns='Product', values='TotalSales', aggfunc='sum').fillna(0)

# Plot stacked bar chart
store_product.plot(kind='bar', stacked=True, figsize=(10,6), colormap='tab20')
plt.title("Stacked Bar Chart: Product Sales per Store")
plt.ylabel("Total Sales")
plt.xlabel("Store")
plt.legend(title="Product", bbox_to_anchor=(1.05, 1))
plt.show()

# COMMAND ----------

import seaborn as sns

plt.figure(figsize=(8,5))
sns.boxplot(x='Product', y='Price', data=retail_df, palette='Set3')
plt.title("Box Plot: Price Distribution per Product")
plt.ylabel("Price")
plt.xlabel("Product")
plt.show()

# COMMAND ----------

plt.figure(figsize=(8,5))
sns.violinplot(x='Product', y='Quantity', data=retail_df, palette='Pastel1')
plt.title("Violin Plot: Quantity Distribution per Product")
plt.ylabel("Quantity")
plt.xlabel("Product")
plt.show()

# COMMAND ----------

sns.pairplot(retail_df[['Quantity', 'Price', 'TotalSales']], kind='scatter', diag_kind='kde', plot_kws={'alpha':0.6})
plt.suptitle("Pair Plot: Quantity, Price, TotalSales", y=1.02)
plt.show()