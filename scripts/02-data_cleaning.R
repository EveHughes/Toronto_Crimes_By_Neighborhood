#### Preamble ####
# Purpose: Cleans the raw data
# Author: Bruce Zhang
# Date: 23 September 2024
# Contact: brucejc.zhang@mail.utoronto.ca
# License: MIT
# Pre-requisites: None
# Any other information needed? None

#### Workspace setup ####
library(tidyverse)
library(dplyr)
library(readr)

#### Clean data ####
# Read raw_data.csv as raw_data
raw_data <- read_csv("data/raw_data/raw_data.csv")

# Re-assign column names for clarity
colnames(raw_data) <- c("neighbourhood", "neighbourhood_id", "arsons", "assaults",
                        "break_and_enters", "drug_arrests", "fire_medical_calls", 
                        "fire_vehicle_incidents", "fires_alarms", "hazardous_incidents",
                        "murders", "robberies", "sexual_assaults", "thefts", 
                        "total_major_crime_incidents", "vehicle_thefts")

# Select columns with data of interest
cleaned_data <- raw_data[-1, ] %>%
  select(neighbourhood, assaults, break_and_enters, 
         drug_arrests, hazardous_incidents, sexual_assaults, thefts,
         total_major_crime_incidents, vehicle_thefts)

# Order data for easier interpretation
ordered_data <- cleaned_data %>%  
  mutate(total_major_crime_incidents = as.numeric(total_major_crime_incidents)) %>%
  arrange(desc(total_major_crime_incidents))

# Select the top 50 results for the purpose of the study (to look at neighbourhoods with high crime numbers)
analysis_data <- ordered_data %>%
  slice(1:50)

#### Save data ####
# Write as "analysis_data.csv"
write_csv(x = analysis_data, file = "data/analysis_data/analysis_data.csv")

