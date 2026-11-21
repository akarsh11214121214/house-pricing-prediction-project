# house-pricing-prediction-project
my project upon the topic of "house pricing prediction" under the HCL training program. demonstration of my learning from the training
# 🏠 House Price Dataset Cleaning System

A Python-based data cleaning and preprocessing project that transforms messy residential property data into a clean, structured dataset using **Pandas and NumPy**.

## 📌 Project Overview

Real-world datasets often contain missing values, duplicate records, inconsistent data types, and unnecessary columns.

This project addresses these data quality issues through a structured data cleaning pipeline.

The system processes a deliberately messy house price dataset and generates a cleaned CSV file suitable for further data analysis.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Visual Studio Code
- Git & GitHub

## ⚙️ Key Features

- Loading and inspecting CSV datasets.
- Detecting and removing duplicate records.
- Identifying and handling duplicate IDs.
- Detecting missing values.
- Removing columns with more than 80% missing values.
- Converting incorrect data types into appropriate formats.
- Handling missing categorical values using mode.
- Handling missing numerical values using median.
- Validating the cleaned dataset.
- Exporting the final cleaned CSV file.

## 🔄 Data Cleaning Workflow

1. Load the input dataset.
2. Analyse missing values and duplicate records.
3. Remove exact duplicate rows.
4. Remove duplicate IDs while retaining the first occurrence.
5. Calculate missing-value percentages.
6. Drop columns exceeding the 80% missing-value threshold.
7. Convert numerical fields into appropriate data types.
8. Handle missing categorical and numerical values.
9. Perform final validation.
10. Export the cleaned dataset.

## 📂 Project Structure

```text
House-Price-Dataset-Cleaning/
│
├── YAHOO.PY
├── house_price_data_messy_for_cleaning.csv
├── house_price_data_cleaning_final.csv
├── House_Price_Data_Cleaning_SRS_Final.docx
└── README.md
```

## ▶️ How to Run

### 1. Install the required libraries

```bash
pip install pandas numpy
```

### 2. Configure the dataset paths

Update the input and output file paths in the Python script according to your system.

### 3. Execute the program

```bash
python YAHOO.PY
```

### 4. Access the output

The cleaned dataset will be exported to the configured output location as a CSV file.

## 🎯 Project Objective

The primary objective is to understand and implement fundamental data cleaning techniques using Python, Pandas, and NumPy while improving the quality and consistency of a real-world-style dataset.

## 👨‍💻 Author
AKARSH VERMA
2026B01010998
akarsh.26b01010998@abes.ac.in

**Akarsh**

Academic Python Data Cleaning Project.
