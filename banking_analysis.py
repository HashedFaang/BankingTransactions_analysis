import pandas as pd
import os
from typing import Optional

# Configuration constants
SUSPICIOUS_AMOUNT_THRESHOLD = 50000
ODD_HOURS_START = 0
ODD_HOURS_END = 5
REQUIRED_COLUMNS = {'customer_id', 'amount', 'timestamp', 'location', 'home_location', 'category'}


def validate_dataframe(df: pd.DataFrame) -> bool:
    """Validate that DataFrame has required columns."""
    return all(col in df.columns for col in REQUIRED_COLUMNS)


def read_banking_data(file_path: str = 'banking_transactions.csv') -> Optional[pd.DataFrame]:
    """Read banking data with validation."""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} was not found.")

        df = pd.read_csv(file_path)
        if not validate_dataframe(df):
            raise ValueError("Missing required columns in the data")

        return df
    except pd.errors.EmptyDataError:
        print("The file is empty")
        return None
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV file: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error reading file: {e}")
        return None


def process_data(df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """Process banking data and add fraud detection flags."""
    try:
        if df is None or df.empty:
            print("No data to process")
            return None

        # Create a copy to avoid modifying original data
        processed_df = df.copy()

        # Clean data
        processed_df = processed_df.dropna()
        processed_df = processed_df.drop_duplicates()

        # Convert timestamp and add flags
        processed_df['timestamp'] = pd.to_datetime(processed_df['timestamp'])
        processed_df['hour'] = processed_df['timestamp'].dt.hour

        # Add detection flags
        processed_df['high_amount_flag'] = processed_df['amount'] > SUSPICIOUS_AMOUNT_THRESHOLD
        processed_df['odd_time_flag'] = processed_df['hour'].between(ODD_HOURS_START, ODD_HOURS_END)
        processed_df['location_flag'] = processed_df['location'] != processed_df['home_location']

        # Calculate suspicious transactions
        processed_df['suspicious'] = (
                processed_df['high_amount_flag'] |
                processed_df['odd_time_flag'] |
                processed_df['location_flag']
        ).astype(int)

        return processed_df

    except Exception as e:
        print(f"Error processing data: {e}")
        return None


def save_suspicious(df: pd.DataFrame, output_path: str = 'bank_suspicious.csv') -> bool:
    """Save suspicious transactions to CSV."""
    try:
        suspicious_df = df[df['suspicious'] == 1]
        suspicious_df.to_csv(output_path, index=False)
        print(f'Saved {len(suspicious_df)} suspicious transactions to {output_path}')
        return True
    except Exception as e:
        print(f"Error saving suspicious transactions: {e}")
        return False


if __name__ == "__main__":
    df = read_banking_data()
    if df is not None:
        processed_df = process_data(df)
        if processed_df is not None:
            save_suspicious(processed_df)