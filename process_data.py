    import pandas as pd

# Load dataset
df = pd.read_csv('data/superstore_dataset.csv')
print(f"Original row count: {len(df)}")

# Clean data
df = df.dropna()  # Handle missing values
df = df.drop_duplicates()  # Remove duplicates
print(f"Cleaned row count: {len(df)}")

# Calculate metrics
total_sales = df['sales'].sum()
profit_margin = (df['profit'].sum() / total_sales) * 100 if total_sales > 0 else 0
sales_by_region = df.groupby('region')['sales'].sum().to_dict()

# Generate report
report = pd.DataFrame({
    'Metric': ['Total Sales', 'Profit Margin (%)', 'Sales by Region'],
    'Value': [total_sales, profit_margin, sales_by_region]
})
report.to_csv('reports/sales_report.csv', index=False)

print(f"Generated report: Total Sales = {total_sales}, Profit Margin = {profit_margin}%, Sales by Region = {sales_by_region}")