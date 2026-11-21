import pandas as pd
import numpy as np

file_path = r"C:\Users\Akarsh\OneDrive\Desktop\house_price_data_messy_for_cleaning.csv"

df = pd.read_csv(file_path)

print("Original Dataset Shape:", df.shape)


print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())


df = df.drop_duplicates()


if "Id" in df.columns:
    df = df.drop_duplicates(subset="Id", keep="first")


missing_percentage = (df.isnull().sum() / len(df)) * 100

columns_to_drop = missing_percentage[
    missing_percentage > 80
].index

df = df.drop(columns=columns_to_drop)


if "Functional" in df.columns:
    df["Functional"] = df["Functional"].fillna("Typ")


if "MSZoning" in df.columns:
    mode_value = df["MSZoning"].mode()

    if not mode_value.empty:
        df["MSZoning"] = df["MSZoning"].fillna(mode_value[0])


if "LotFrontage" in df.columns:

    df["LotFrontage"] = pd.to_numeric(
        df["LotFrontage"], errors="coerce"
    )

    median_value = df["LotFrontage"].median()

    df["LotFrontage"] = df["LotFrontage"].fillna(
        median_value
    )


categorical_columns = df.select_dtypes(
    include=["object", "str"]
).columns

for column in categorical_columns:
    if df[column].isnull().any():
        mode_value = df[column].mode()

        if not mode_value.empty:
            df[column] = df[column].fillna(mode_value[0])
        else:
            df[column] = df[column].fillna("None")


numerical_columns = df.select_dtypes(
    include=[np.number]
).columns

for column in numerical_columns:
    df[column] = df[column].fillna(df[column].median())


print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

if "Id" in df.columns:
    print("\nDuplicate IDs Remaining:",
          df["Id"].duplicated().sum())

print("\nFinal Dataset Shape:", df.shape)


output_path = r"C:\Users\Akarsh\OneDrive\Desktop\house_price_data_messy_for_cleaning.csv"

df.to_csv(output_path, index=False)

print("\nDATA CLEANING COMPLETED SUCCESSFULLY!")
print("Cleaned file saved at:", output_path)