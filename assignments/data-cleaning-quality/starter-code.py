# Starter Code: Data Cleaning and Quality

import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load raw CSV data."""
    return pd.read_csv(path)


def audit_data(df: pd.DataFrame) -> None:
    """Print an initial quality audit of the dataset."""
    print("=== RAW DATA AUDIT ===")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print("\nMissing values by column:")
    print(df.isna().sum())
    print("\nDuplicate rows:", df.duplicated().sum())


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply cleaning rules and return a cleaned DataFrame."""
    cleaned = df.copy()

    # TODO 1: Remove duplicated rows.

    # TODO 2: Handle missing values in at least 2 columns.

    # TODO 3: Standardize city names (trim + title case).

    # TODO 4: Remove or correct invalid scores (outside 0-100).

    return cleaned


def quality_report(before: pd.DataFrame, after: pd.DataFrame) -> None:
    """Print a short report comparing quality before vs after cleaning."""
    print("\n=== QUALITY REPORT ===")
    print(f"Rows before: {len(before)}")
    print(f"Rows after:  {len(after)}")
    print(f"Duplicates before: {before.duplicated().sum()}")
    print(f"Duplicates after:  {after.duplicated().sum()}")

    before_missing = before.isna().sum()
    after_missing = after.isna().sum()

    print("\nMissing values resolved by column:")
    print(before_missing - after_missing)


def main() -> None:
    raw_df = load_data("data.csv")

    audit_data(raw_df)

    cleaned_df = clean_data(raw_df)
    cleaned_df.to_csv("clean_data.csv", index=False)

    quality_report(raw_df, cleaned_df)
    print("\nSaved cleaned dataset to clean_data.csv")


if __name__ == "__main__":
    main()
