# IPL Dataset Handling & Preprocessing with Pandas

This repository contains Python scripts demonstrating various data loading, handling, and preprocessing techniques using the **Pandas** library on an IPL (Indian Premier League) dataset.

## 📌 Project Overview

The main objective of this project is to showcase how to clean, manipulate, and handle real-world dataset edge cases such as missing values, bad lines, data type conversions, and custom value mapping during the file ingestion phase.

## 🚀 Features & Techniques Covered

- **Custom Path & Delimiter Handling:** Reading `.csv` and `.tsv` files smoothly while avoiding Unicode string escape errors.
- **Data Inspection:** Checking datasets using `.dtypes`, `.info()`, and `.head()`.
- **Handling Missing Data (`NaN` / `NA`):** Filtering out incomplete rows using `.dropna()` and handling missing integer values using Pandas' nullable `Int64` data type.
- **Column Customization & Renaming:** Applying custom functions using `converters` during file loading.
- **Date Handling:** Converting date and season columns into standard `datetime` formats using `parse_dates`.
- **Handling Bad Lines & Corrupt Data:** Dealing with inconsistent fields and skipping malformed rows.

## 🛠️ Requirements

Make sure you have Python installed along with the Pandas package:

```bash
pip install pandas
