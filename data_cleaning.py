
import pandas as pd


# STEP 1: LOAD DATASET

def load_data():

    df = pd.read_csv(
        "zomato.csv",
        encoding="latin-1"
    )

    print("Zomato Dataset Loaded Successfully!")

    print("\nFirst 5 Records:")
    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    return df


# STEP 2: CHECK MISSING VALUES

def check_missing_values(df):

    print("\nMissing Values:")
    print(df.isnull().sum())


# STEP 3: REMOVE DUPLICATES

def remove_duplicates(df):

    df.drop_duplicates(inplace=True)

    print("\nDuplicate Records Removed!")

    return df


# STEP 4: HANDLE MISSING VALUES

def handle_missing_values(df):

    df.dropna(subset=["Cuisines"], inplace=True)

    print("\nMissing Cuisine Values Removed!")

    return df


# STEP 5: CLEAN DATA

def clean_data(df):

    print("\nStarting Data Cleaning...")

    check_missing_values(df)

    df = remove_duplicates(df)

    df = handle_missing_values(df)

    print("\nData Cleaning Completed!")

    print("Final Dataset Shape:", df.shape)

    return df
