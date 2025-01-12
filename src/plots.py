"""
This script analyzes Best Buy product data for headphones and laptops. It performs the following steps:

1. Imports necessary libraries for data manipulation and visualization.
2. Loads scraped data from CSV files into Pandas DataFrames.
3. Calculates average and total discount percentages and cash amounts for both headphones and laptops.
4. Organizes the calculated metrics into a new DataFrame.
5. Visualizes the average and total cash amounts using bar plots with Seaborn and Matplotlib.
6. Displays the generated plots.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load scraped data from CSV files into DataFrames
df_headphones = pd.read_csv('data/data_headphones.csv')
df_laptops = pd.read_csv('data/data_laptops.csv')

# Calculate average discount percentages and cash amounts
avg_discount_percent_h = round(df_headphones['Discount Percentage'][:56].mean())
avg_discount_percent_l = round(df_laptops['Discount Percentage'].mean())
avg_cash_amount_h = round(df_headphones['Saved Amount'][:56].mean())
avg_cash_amount_l = round(df_laptops['Saved Amount'].mean())

# Calculate total cash amounts
total_cash_amount_h = df_headphones['Saved Amount'].sum()
total_cash_amount_l = df_laptops['Saved Amount'].sum()

# Create a new DataFrame to hold the calculated metrics
df = pd.DataFrame({
    'x_title': ['Average Cash Amount(USD)', 'Total Cash Amount(USD)'],
    'x_axis': ['HeadPhones', 'Laptops'],
    'ColumnsA': [avg_cash_amount_h, avg_cash_amount_l],
    'ColumnsB': [total_cash_amount_h, total_cash_amount_l]
})

# Set the theme for Seaborn plots
sns.set_theme(style="whitegrid")

# Create subplots for visualizing average and total cash amounts
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))

# Plot average cash amounts
sns.barplot(x='x_axis', y='ColumnsA', data=df, ax=axes[0])
axes[0].set_ylabel("")
axes[0].set_xlabel(df.x_title[0])

# Plot total cash amounts with average discount percentages in the y-label
sns.barplot(x='x_axis', y='ColumnsB', data=df, ax=axes[1])
axes[1].set_ylabel(f"                                                  Average Discount Percent for Headphones & Laptops(BestBuy): {avg_discount_percent_h}%")
axes[1].set_xlabel(df.x_title[1])

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
