#### Preamble ####
# Purpose: Tests the data
# Author: Bruce Zhang
# Date: 23 September 2024
# Contact: brucejc.zhang@mail.utoronto.ca
# License: MIT
# Pre-requisites: None
# Any other information needed? None


#### Workspace setup ####
library(tidyverse)
library(dplyr)

analysis_data <- read_csv("data/analysis_data/analysis_data.csv")

# Created summary statistics (EDA) of data set
summary(analysis_data)

# Check for any missing data values
analysis_data %>%
  summarise_all(~sum(is.na(.)))

# Visualize data by creating a simple scatter plot
library(ggplot2)
ggplot(analysis_data, aes(x = neighbourhood, y = total_major_crime_incidents)) +
  geom_point()

# Check for duplicates (not an issue in our case, just to get an idea)
analysis_data %>%
  filter(duplicated(.))

# Check for unique values (not an issue in our case, just to get an idea)
analysis_data %>%
  summarise_all(~n_distinct(.))

# Check first few rows of analysis_data
head(analysis_data)
