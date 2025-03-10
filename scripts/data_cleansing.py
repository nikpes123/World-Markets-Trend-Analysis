import pandas as pd
import os

def load_data(file_path):
    """Load stock market data from CSV."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return pd.read_csv(file_path)

def clean_data(df):
    """Preprocess the dataset by handling missing values, converting data types, and removing duplicates."""
    # Convert 'Date' to datetime format
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Drop rows with invalid dates
    df = df.dropna(subset=["Date"])

    # Forward-fill missing values for stock prices
    df.fillna(method="ffill", inplace=True)

    # Remove duplicates (if any)
    df.drop_duplicates(inplace=True)

    return df

def save_cleaned_data(df, output_path="data/processed_data.csv"):
    """Save cleaned dataset to CSV."""
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to: {output_path}")

if __name__ == "__main__":
    # File path to raw dataset
    input_file = "data/indexData.csv"
    
    # Load and clean data
    stock_data = load_data(input_file)
    cleaned_data = clean_data(stock_data)

    # Save processed data
    save_cleaned_data(cleaned_data)
