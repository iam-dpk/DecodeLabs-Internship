# DecodeLabs Data Analytics Internship — Project 1

## Data Cleaning & Preparation

This project was completed as part of the **DecodeLabs Data Analytics Internship**.

The purpose of this project was to clean, validate, and prepare an e-commerce dataset so that it could be used reliably for further data analysis.

---

## 🎯 Project Objective

The main objective was to identify and resolve common data-quality issues, including:

- Missing values
- Duplicate records
- Duplicate Order IDs
- Incorrect or inconsistent date formats
- Numeric data consistency
- Overall dataset quality

The final goal was to produce a clean and analysis-ready dataset.

---

## 📊 Dataset Overview



<img width="1152" height="810" alt="Screenshot 2026-09-30 204119" src="https://github.com/user-attachments/assets/a3c393d7-2414-4e4a-8ad1-ac68c1946857" />







The original dataset contains:

- **1,200 records**
- **14 columns**

### Columns

| Column | Description |
|---|---|
| OrderID | Unique order identifier |
| Date | Order date |
| CustomerID | Customer identifier |
| Product | Product purchased |
| Quantity | Quantity ordered |
| UnitPrice | Price per unit |
| ShippingAddress | Customer shipping address |
| PaymentMethod | Payment method used |
| OrderStatus | Current order status |
| TrackingNumber | Shipment tracking number |
| ItemsInCart | Number of items in the cart |
| CouponCode | Coupon applied to the order |
| ReferralSource | Source through which the customer arrived |
| TotalPrice | Total order price |

---

## 🧹 Data Cleaning Process

The dataset was reviewed and cleaned through the following checks:

### 1. Date Validation

All date values were checked to ensure they were valid Excel date values.

- **1,200 date values checked**
- **0 invalid dates**
- Dates standardized for consistent display using `YYYY-MM-DD`

### 2. Duplicate Check

The dataset was checked for both exact duplicate records and duplicate Order IDs.

- **Exact duplicate rows: 0**
- **Duplicate Order IDs: 0**

### 3. Numeric Data Validation

Numeric fields such as:

- Quantity
- UnitPrice
- TotalPrice

were reviewed for consistency and suitability for further analysis.

### 4. Missing Values

Relevant fields were reviewed for missing values.

No values were artificially created or changed without a valid data-supported reason.

<img width="1832" height="682" alt="Screenshot 2026-09-30 204137" src="https://github.com/user-attachments/assets/dfba9370-82d5-4c3d-bef5-bdcc47beff9a" />


---

## ✅ Data Quality Results

| Quality Check | Result |
|---|---:|
| Total records | 1,200 |
| Total columns | 14 |
| Exact duplicate rows | 0 |
| Duplicate Order IDs | 0 |
| Invalid date values | 0 |
| Date values standardized | 1,200 |
| Missing TotalPrice values filled | 0 |

---

## 📁 Project Files

<img width="1900" height="661" alt="Screenshot 2026-09-30 204152" src="https://github.com/user-attachments/assets/8a72bd21-728d-4176-8dbd-cfa6c8485fce" />

The project follows a clear three-stage workflow:

```text
Original Dataset
       ↓
Cleaned Dataset
       ↓
Final Dataset




