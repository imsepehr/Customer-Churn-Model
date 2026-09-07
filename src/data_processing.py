import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load the raw Telco Customer Churn dataset."""
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the raw Telco Customer Churn dataset.

    Cleaning steps:
    - Remove leading/trailing whitespace from column names.
    - Convert TotalCharges to numeric.
    - Handle missing TotalCharges values.
    - Remove the customerID identifier.

    Note:
    Encoding, scaling, and other model-specific preprocessing
    are intentionally handled in later phases.
    """

    df = df.copy()

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert TotalCharges from object to numeric
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # Handle missing TotalCharges
    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    # Remove identifier column
    df = df.drop(columns=["customerID"])

    return df