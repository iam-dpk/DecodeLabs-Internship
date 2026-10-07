# DecodeLabs Internship — Project 2: Exploratory Data Analysis

## Overview
This project performs Exploratory Data Analysis (EDA) on the provided final dataset to understand distributions, descriptive statistics, missing values, outliers, and important categorical patterns.

## Dataset
- Source file: `data/Final Dataset.xlsx`
- Worksheet analyzed: `Cleaned_Data`
- Rows: **1,200**
- Columns: **14**

## Analysis Covered
- Dataset structure and data types
- Count, mean, median and descriptive statistics
- Missing-value analysis
- Duplicate-row check
- IQR-based outlier detection
- Categorical frequency analysis
- Distribution and comparison visualizations
- Key observations

## Key Observations
- Dataset contains 1,200 rows and 14 columns.
- Duplicate rows: 0.
- Missing values are concentrated in: CouponCode (309).
- Average TotalPrice: 1,053.97; median: 823.62.
- Average Quantity: 2.95; median: 3.00.
- Most frequent Product: Printer.
- Most frequent PaymentMethod: Online.
- Most frequent OrderStatus: Cancelled.
- Most frequent ReferralSource: Instagram.

## Project Structure
```text
DecodeLabs_Project2_Final/
├── data/
│   └── Final Dataset.xlsx
├── notebooks/
│   └── DecodeLabs_Project2_EDA.ipynb
├── outputs/
│   ├── EDA_Summary.xlsx
│   ├── EDA_Column_Profile.xlsx
│   ├── EDA_Numeric_Statistics.xlsx
│   └── EDA_Outliers.xlsx
├── images/
├── src/
├── README.md
└── requirements.txt
```

## Tools & Technologies
Python, Pandas, NumPy, Matplotlib, OpenPyXL, Jupyter Notebook.

## How to Run
1. Install dependencies:
   `pip install -r requirements.txt`
2. Open `notebooks/DecodeLabs_Project2_EDA.ipynb`.
3. Run the cells in order.

## Note
The dataset is included for project reproducibility. Redistribution should follow the dataset's original licensing/usage terms.
