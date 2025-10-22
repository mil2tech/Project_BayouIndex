import os
import json
import re
import requests
import pandas as pd
from dotenv import load_dotenv


# ---------------------------- Configuration ---------------------------- #
BLS_ENDPOINT = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
SERIES_ID = "APUS37B74714"  # test series
START_YEAR = "2020"
END_YEAR = "2024"
TIMEOUT_SECONDS = 30


# ---------------------------- Helper Function ---------------------------- #
def fetch_bls_series(series_id: str, start_year: str, end_year: str) -> pd.DataFrame:
    """
    Fetch and normalize data for a single BLS series.

    Args:
        series_id (str): BLS series ID (e.g., 'APUS37B74714').
        start_year (str): Start year (YYYY).
        end_year (str): End year (YYYY).

    Returns:
        pd.DataFrame: Tidy DataFrame with metadata and monthly records.
    """
    # Load API key from .env or API_Keys.env
    load_dotenv(dotenv_path="API_Keys.env")
    API_KEY = os.getenv("BLS_API_KEY")
    if not API_KEY:
        raise EnvironmentError("Missing BLS_API_KEY in API_Keys.env")

    # Build payload
    payload = {
        "seriesid": [series_id],
        "startyear": start_year,
        "endyear": end_year,
        "registrationkey": API_KEY,
        "catalog": True
    }

    # API request
    response = requests.post(
        BLS_ENDPOINT,
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload),
        timeout=TIMEOUT_SECONDS
    )
    response.raise_for_status()

    data = response.json()
    if data.get("status") != "REQUEST_SUCCEEDED":
        raise ValueError(f"BLS API error: {data.get('message')}")

    # Extract data
    series = data["Results"]["series"][0]
    catalog = series.get("catalog", {}) or {}

    # Metadata (with safe fallbacks)
    title = catalog.get("series_title", "")
    area = catalog.get("area_name", catalog.get("area", ""))
    item = catalog.get("item_name", catalog.get("item", ""))

    # Fallback: parse area/item from title if missing
    if (not area or not item) and title:
        m = re.search(r"^(?P<item>.+?)\s+in\s+(?P<area>.+?),\s+average price", title, flags=re.IGNORECASE)
        if m:
            item = item or m.group("item").strip()
            area = area or m.group("area").strip()

    # Build rows
    rows = []
    for obs in series.get("data", []):
        period = obs.get("period", "")
        if not (period.startswith("M") and period != "M13"):  # monthly only
            continue
        rows.append({
            "SeriesID": series.get("seriesID"),
            "Year": int(obs["year"]),
            "Month": int(period[1:]),
            "Period": period,
            "Value": float(obs["value"]),
            "Title": title,
            "Area": area,
            "Item": item
        })

    # Create DataFrame
    df = pd.DataFrame(rows)
    if df.empty:
        return df

    df["Date"] = pd.to_datetime(dict(year=df["Year"], month=df["Month"], day=1))
    df = (
        df[["Date", "Year", "Month", "Period", "SeriesID", "Title", "Area", "Item", "Value"]]
        .sort_values(["SeriesID", "Date"])
        .reset_index(drop=True)
    )

    return df


# ---------------------------- Main Block ---------------------------- #
if __name__ == "__main__":
    try:
        df = fetch_bls_series(SERIES_ID, START_YEAR, END_YEAR)
        print("✅ Data successfully retrieved and normalized.\n")
        print(df.head(12))
        df.to_csv(f"bls_sample_{SERIES_ID}_{START_YEAR}_{END_YEAR}.csv", index=False)
        print(f"\n💾 Saved to: bls_sample_{SERIES_ID}_{START_YEAR}_{END_YEAR}.csv")
    except Exception as e:
        print(f"❌ Error: {e}")
