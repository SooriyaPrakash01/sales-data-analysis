import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales_data.csv")

print("Dataset:")
print(data)

# Total revenue by product
product_sales = data.groupby("Product")["Revenue"].sum()
print("\nTotal Revenue by Product:")
print(product_sales)

# Monthly revenue
monthly_sales = data.groupby("Month")["Revenue"].sum()
print("\nMonthly Revenue:")
print(monthly_sales)

# Plot Product Revenue
product_sales.plot(kind='bar')
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()
