
import os
import random
import pandas as pd

# ==========================================
# GEOPULSE - SYNTHETIC DATA GENERATOR
# ==========================================

# Project folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Reproducible random data
random.seed(42)

# ==========================================
# CITY COORDINATE RANGES
# Approximate city study areas, not boundaries
# ==========================================

CITIES = {
    "Hyderabad": {
        "state": "Telangana",
        "lat_min": 17.20, "lat_max": 17.55,
        "lon_min": 78.25, "lon_max": 78.65
    },
    "Bengaluru": {
        "state": "Karnataka",
        "lat_min": 12.80, "lat_max": 13.15,
        "lon_min": 77.40, "lon_max": 77.75
    },
    "Chennai": {
        "state": "Tamil Nadu",
        "lat_min": 12.90, "lat_max": 13.20,
        "lon_min": 80.10, "lon_max": 80.35
    },
    "Mumbai": {
        "state": "Maharashtra",
        "lat_min": 18.90, "lat_max": 19.25,
        "lon_min": 72.75, "lon_max": 73.05
    },
    "Delhi": {
        "state": "Delhi",
        "lat_min": 28.45, "lat_max": 28.75,
        "lon_min": 76.95, "lon_max": 77.35
    },
    "Kolkata": {
        "state": "West Bengal",
        "lat_min": 22.45, "lat_max": 22.70,
        "lon_min": 88.25, "lon_max": 88.45
    },
    "Pune": {
        "state": "Maharashtra",
        "lat_min": 18.40, "lat_max": 18.65,
        "lon_min": 73.75, "lon_max": 74.00
    },
    "Ahmedabad": {
        "state": "Gujarat",
        "lat_min": 22.95, "lat_max": 23.15,
        "lon_min": 72.45, "lon_max": 72.70
    },
    "Jaipur": {
        "state": "Rajasthan",
        "lat_min": 26.80, "lat_max": 27.05,
        "lon_min": 75.70, "lon_max": 76.00
    },
    "Lucknow": {
        "state": "Uttar Pradesh",
        "lat_min": 26.75, "lat_max": 27.00,
        "lon_min": 80.85, "lon_max": 81.10
    }
}

# ==========================================
# DATA GENERATION SETTINGS
# ==========================================

RETAIL_PER_CITY = 350
MOBILITY_PER_CITY = 150

RETAIL_CATEGORIES = [
    "Supermarket",
    "Convenience Store",
    "Grocery Store",
    "Clothing Store"
]

MOBILITY_TYPES = [
    "Bus Stop",
    "Metro Station",
    "Railway Station",
    "Public Transport Platform"
]

RETAIL_PREFIXES = [
    "Fresh Mart",
    "City Market",
    "Smart Store",
    "Daily Needs",
    "Fashion Point",
    "Mega Mart",
    "Urban Shop",
    "Retail Hub"
]

MOBILITY_PREFIXES = [
    "Central",
    "City",
    "Main Road",
    "Market",
    "Junction",
    "North",
    "South",
    "East"
]

# ==========================================
# GENERATE RETAIL DATA
# ==========================================

def generate_retail_data():

    records = []

    print("\nGenerating synthetic retail data...")

    for city, details in CITIES.items():

        for i in range(1, RETAIL_PER_CITY + 1):

            category = random.choice(RETAIL_CATEGORIES)

            record = {
                "retail_id": f"RET_{city[:3].upper()}_{i:04d}",
                "city": city,
                "state": details["state"],
                "store_name": (
                    f"{random.choice(RETAIL_PREFIXES)} {i}"
                ),
                "category": category,
                "latitude": round(
                    random.uniform(
                        details["lat_min"],
                        details["lat_max"]
                    ), 6
                ),
                "longitude": round(
                    random.uniform(
                        details["lon_min"],
                        details["lon_max"]
                    ), 6
                ),
                "simulated_daily_visitors": random.randint(20, 1500),
                "data_source": "Synthetic",
                "is_synthetic": True
            }

            records.append(record)

        print(f"{city}: {RETAIL_PER_CITY} retail records generated")

    return pd.DataFrame(records)


# ==========================================
# GENERATE MOBILITY DATA
# ==========================================

def generate_mobility_data():

    records = []

    print("\nGenerating synthetic mobility data...")

    for city, details in CITIES.items():

        for i in range(1, MOBILITY_PER_CITY + 1):

            mobility_type = random.choice(MOBILITY_TYPES)

            record = {
                "mobility_id": f"MOB_{city[:3].upper()}_{i:04d}",
                "city": city,
                "state": details["state"],
                "location_name": (
                    f"{random.choice(MOBILITY_PREFIXES)} "
                    f"{mobility_type} {i}"
                ),
                "mobility_type": mobility_type,
                "latitude": round(
                    random.uniform(
                        details["lat_min"],
                        details["lat_max"]
                    ), 6
                ),
                "longitude": round(
                    random.uniform(
                        details["lon_min"],
                        details["lon_max"]
                    ), 6
                ),
                "simulated_daily_passengers": random.randint(50, 5000),
                "data_source": "Synthetic",
                "is_synthetic": True
            }

            records.append(record)

        print(f"{city}: {MOBILITY_PER_CITY} mobility records generated")

    return pd.DataFrame(records)


# ==========================================
# VALIDATE AND SAVE DATA
# ==========================================

def save_datasets(retail_df, mobility_df):

    # Remove duplicate IDs
    retail_df = retail_df.drop_duplicates(subset=["retail_id"])
    mobility_df = mobility_df.drop_duplicates(subset=["mobility_id"])

    # Check missing values
    print("\nChecking missing values...")

    print("Retail missing values:", retail_df.isnull().sum().sum())
    print("Mobility missing values:", mobility_df.isnull().sum().sum())

    # Save raw datasets
    retail_df.to_csv(
        os.path.join(RAW_DIR, "retail_all_cities.csv"),
        index=False
    )

    mobility_df.to_csv(
        os.path.join(RAW_DIR, "mobility_all_cities.csv"),
        index=False
    )

    # Save processed datasets
    retail_df.to_csv(
        os.path.join(PROCESSED_DIR, "india_retail_locations.csv"),
        index=False
    )

    mobility_df.to_csv(
        os.path.join(PROCESSED_DIR, "india_mobility_locations.csv"),
        index=False
    )

    print("\nDatasets saved successfully!")


# ==========================================
# MAIN FUNCTION
# ==========================================

def main():

    print("=" * 50)
    print("GEOPULSE - RETAIL MOBILITY ANALYTICS")
    print("SYNTHETIC DATA GENERATION")
    print("=" * 50)

    retail_df = generate_retail_data()
    mobility_df = generate_mobility_data()

    save_datasets(retail_df, mobility_df)

    print("\n" + "=" * 50)
    print("FINAL DATASET SUMMARY")
    print("=" * 50)

    print("Total cities:", len(CITIES))
    print("Total retail records:", len(retail_df))
    print("Total mobility records:", len(mobility_df))
    print("Total records:", len(retail_df) + len(mobility_df))

    print("\nRetail records by city:")
    print(retail_df.groupby("city").size())

    print("\nMobility records by city:")
    print(mobility_df.groupby("city").size())

    print("\nRetail category distribution:")
    print(retail_df["category"].value_counts())

    print("\nMobility type distribution:")
    print(mobility_df["mobility_type"].value_counts())

    print("\nGeoPulse data generation completed!")


if __name__ == "__main__":
    main()
