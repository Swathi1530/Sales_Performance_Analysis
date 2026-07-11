import pandas as pd
import matplotlib.pyplot as plt

# ======================================
# SALES PERFORMANCE ANALYSIS SYSTEM
# ======================================

print("======================================")
print(" SALES PERFORMANCE ANALYSIS SYSTEM")
print("======================================")

print("\nLoading Dataset...\n")

# Load CSV File
df = pd.read_csv("sales_data.csv")

print("Dataset Loaded Successfully!\n")

print("Sales Dataset:\n")
print(df)

# ======================================
# DATASET INFORMATION
# ======================================

print("\n======================================")
print("DATASET INFORMATION")
print("======================================")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

# ======================================
# DATA CLEANING
# ======================================

print("\n======================================")
print("DATA CLEANING")
print("======================================")

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

df = df.dropna()

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nData Cleaning Completed Successfully!")

# ======================================
# SALES ANALYSIS
# ======================================

print("\n======================================")
print("SALES ANALYSIS")
print("======================================")

df["Sales"] = df["Quantity"] * df["Price"]

print("\nDataset with Sales Column:")
print(df)

total_sales = df["Sales"].sum()
total_quantity = df["Quantity"].sum()

print("\nTotal Sales : ₹", total_sales)
print("Total Quantity Sold :", total_quantity)

# ======================================
# TOP SELLING PRODUCT
# ======================================

print("\n======================================")
print("TOP SELLING PRODUCT")
print("======================================")

product_sales = df.groupby("Product")["Sales"].sum()

print("\nSales by Product:")
print(product_sales)

top_product = product_sales.idxmax()
top_sales = product_sales.max()

print("\nTop Selling Product :", top_product)
print("Sales Amount : ₹", top_sales)

# ======================================
# CATEGORY-WISE SALES ANALYSIS
# ======================================

print("\n======================================")
print("CATEGORY-WISE SALES ANALYSIS")
print("======================================")

category_sales = df.groupby("Category")["Sales"].sum()

print("\nCategory-wise Sales:")
print(category_sales)

top_category = category_sales.idxmax()
top_category_sales = category_sales.max()

print("\nBest Performing Category :", top_category)
print("Category Sales : ₹", top_category_sales)

# ======================================
# MONTHLY SALES ANALYSIS
# ======================================

print("\n======================================")
print("MONTHLY SALES ANALYSIS")
print("======================================")

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month_name()

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# ======================================
# GENERATING CHARTS
# ======================================

print("\n======================================")
print("GENERATING CHARTS")
print("======================================")

# Bar Chart
plt.figure(figsize=(6,4))
category_sales.plot(kind="bar", color="skyblue")
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# Line Chart
plt.figure(figsize=(6,4))
monthly_sales.plot(kind="line", marker="o", color="green")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

# Pie Chart
plt.figure(figsize=(6,6))
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.show()

print("\nCharts Generated Successfully!")

# ======================================
# GENERATING REPORT
# ======================================

print("\n======================================")
print("GENERATING REPORT")
print("======================================")

with open("report.txt", "w", encoding="utf-8") as report:

    report.write("SALES PERFORMANCE ANALYSIS REPORT\n")
    report.write("=" * 40 + "\n\n")

    report.write(f"Total Sales : ₹{total_sales}\n")
    report.write(f"Total Quantity Sold : {total_quantity}\n\n")

    report.write(f"Top Selling Product : {top_product}\n")
    report.write(f"Sales Amount : ₹{top_sales}\n\n")

    report.write(f"Best Performing Category : {top_category}\n")
    report.write(f"Category Sales : ₹{top_category_sales}\n\n")

    report.write("Monthly Sales\n")
    report.write("-" * 30 + "\n")

    for month, sales in monthly_sales.items():
        report.write(f"{month} : ₹{sales}\n")

print("\nReport Generated Successfully!")
print("Report saved as report.txt")

print("\nProject Completed Successfully!")