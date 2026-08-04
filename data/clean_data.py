import argparse
import logging
import sys
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


def load_data(path):
    """Read the raw social media export into a DataFrame."""
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        log.error("Input file not found: %s", path)
        sys.exit(1)


def clean(df):
    """Drop empty and duplicate rows, normalise text, and parse dates."""
    before = len(df)
    df = df.dropna(subset=["tweet_text", "sentiment"]).drop_duplicates()
    df["tweet_text"] = df["tweet_text"].str.strip().str.lower()
    df["post_date"] = pd.to_datetime(df["post_date"], errors="coerce")
    df = df.dropna(subset=["post_date"])
    log.info("Removed %d rows during cleaning", before - len(df))
    return df


def summarise(df):
    """Return post counts and share by sentiment."""
    summary = df.groupby("sentiment").size().reset_index(name="total_posts")
    summary["share_pct"] = (summary["total_posts"] / len(df) * 100).round(2)
    return summary


def main():
    parser = argparse.ArgumentParser(description="Clean social media data for the Azure pipeline")
    parser.add_argument("--input", default="data.csv")
    parser.add_argument("--output", default="cleaned_data.csv")
    args = parser.parse_args()

    df = clean(load_data(args.input))
    df.to_csv(args.output, index=False)
    log.info("Wrote %d clean rows to %s", len(df), args.output)
    print(summarise(df).to_string(index=False))


if __name__ == "__main__":
    main()
