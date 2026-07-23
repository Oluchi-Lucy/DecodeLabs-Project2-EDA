# DecodeLabs Project 2 - Exploratory Data Analysis (EDA)

Week 2/3 task: performed exploratory data analysis on a 1,200-row
e-commerce dataset using Python (pandas, matplotlib, seaborn).

## What the script does:
- Loads the dataset and displays first 5 rows
- Shows dataset shape and column names
- Calculates basic statistics (mean, median, min, max, quartiles)
- Detects outliers in TotalPrice using a boxplot
- Checks for missing values and duplicate rows
- Analyzes correlations between Quantity, UnitPrice, ItemsInCart, and TotalPrice
- Summarizes key business observations

## Key findings:
- Average order value: ₦1,053.97 (median: ₦823.62)
- A few high-value outlier orders (up to ₦3,456.40)
- No duplicate rows; only CouponCode has missing values (309 of 1,200)
- TotalPrice is most strongly correlated with UnitPrice (0.72) and Quantity (0.62)
