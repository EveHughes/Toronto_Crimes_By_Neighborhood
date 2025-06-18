#### Preamble ####
# Purpose: Cleans the raw data
# Author: Bruce Zhang (translated to Python)
# Date: 23 September 2024
# Contact: brucejc.zhang@mail.utoronto.ca
# License: MIT

import pandas as pd

#### Clean data ####
# Read raw data
raw_data = pd.read_csv("data/raw_data/raw_data.csv")

# Rename columns for clarity
raw_data.columns = [
    "neighbourhood", "neighbourhood_id", "arsons", "assaults",
    "break_and_enters", "drug_arrests", "fire_medical_calls", 
    "fire_vehicle_incidents", "fires_alarms", "hazardous_incidents",
    "murders", "robberies", "sexual_assaults", "thefts", 
    "total_major_crime_incidents", "vehicle_thefts"
]

# Drop the first row (if it's not actual data)
cleaned_data = raw_data.iloc[1:, :]

# Select relevant columns
cleaned_data = cleaned_data[[
    "neighbourhood", "assaults", "break_and_enters", "drug_arrests",
    "hazardous_incidents", "sexual_assaults", "thefts",
    "total_major_crime_incidents", "vehicle_thefts"
]]

# Convert total_major_crime_incidents to numeric (handle errors safely)
cleaned_data["total_major_crime_incidents"] = pd.to_numeric(
    cleaned_data["total_major_crime_incidents"], errors="coerce"
)

# Sort by descending total crime
ordered_data = cleaned_data.sort_values(
    by="total_major_crime_incidents", ascending=False
)

# Take top 50 rows
analysis_data = ordered_data.head(50)

# Save cleaned data
analysis_data.to_csv("data/analysis_data/analysis_data.csv", index=False)