#### Preamble ####
# Purpose: Simulates Crime-related Data for Different Neighborhoods in Toronto
# Author: Bruce Zhang
# Date: 23 September 2024
# Contact: brucejc.zhang@mail.utoronto.ca
# License: MIT
# Pre-requisites: None
# Any other information needed? None


#### Workspace setup ####
library(dplyr)
library(tibble)

#### Simulate data ####
set.seed(0307)

num_neighbourhoods <- 50

simulated_data <- tibble(
  Neighbourhood = paste("Neighbourhood", 1:num_neighbourhoods),
  Neighbourhood_Id = 1:num_neighbourhoods,
  Arsons = sample(0:10, num_neighbourhoods, replace = TRUE),
  Assaults = sample(50:500, num_neighbourhoods, replace = TRUE),
  `Break & Enters` = sample(20:200, num_neighbourhoods, replace = TRUE),
  `Drug Arrests` = sample(10:100, num_neighbourhoods, replace = TRUE),
  `Fire Medical Calls` = sample(100:1500, num_neighbourhoods, replace = TRUE),
  `Fire Vehicle Incidents` = sample(10:500, num_neighbourhoods, replace = TRUE),
  `Fires & Fire Alarms` = sample(50:700, num_neighbourhoods, replace = TRUE),
  `Hazardous Incidents` = sample(10:200, num_neighbourhoods, replace = TRUE),
  Murders = sample(0:5, num_neighbourhoods, replace = TRUE),
  Robberies = sample(10:100, num_neighbourhoods, replace = TRUE),
  `Sexual Assaults` = sample(5:50, num_neighbourhoods, replace = TRUE),
  Thefts = sample(5:50, num_neighbourhoods, replace = TRUE),
  `Total Major Crime Incidents` = sample(100:1500, num_neighbourhoods, replace = TRUE),
  `Vehicle Thefts` = sample(10:300, num_neighbourhoods, replace = TRUE)
)

print(simulated_data)



