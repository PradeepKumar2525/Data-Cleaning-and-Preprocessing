Data Extraction and Cleaning Process
Extracted raw data from a compressed CSV file into a pandas DataFrame.

Inspected the dataset for missing values and duplicate entries.

Removed duplicates to ensure data integrity.

Standardized column headers by cleaning names (removing spaces/special characters and applying consistent casing).

Cleaned categorical data by replacing shorthand codes (e.g., ‘m’/’f’) with full descriptive labels (‘male’/’female’).

Simplified complex category labels (e.g., from “youth(<25)” to “youth”) for clarity.

Converted date columns from strings to datetime objects, ensuring correct day-month-year interpretation and uniform formatting (dd/mm/yyyy).

Calculated Revenue,Profit from Cost,Quantity and Price

Converted data types appropriately for numeric and date fields to enable analysis.

Removed irrelevant columns to keep the dataset focused and concise.

Finalized the cleaned dataset, making it ready for further analysis or machine learning tasks.
