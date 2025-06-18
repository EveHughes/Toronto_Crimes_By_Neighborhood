#### Preamble ####
# Purpose: Simulates Crime-related Data for Different Neighborhoods in Toronto
# Author: Bruce Zhang (translated to Python)
# Date: 23 September 2024
# Contact: brucejc.zhang@mail.utoronto.ca
# License: MIT
# Pre-requisites: pandas, numpy

#### Workspace setup ####
import pandas as pd
import numpy as np

#### Simulate data ####
np.random.seed(307)

# Set number of observations to simulate
num_neighbourhoods = 50

# Simulate data
simulated_data = pd.DataFrame({
    "Neighbourhood": [f"Neighbourhood {i}" for i in range(1, num_neighbourhoods + 1)],
    "Neighbourhood_Id": np.arange(1, num_neighbourhoods + 1),
    "Arsons": np.random.randint(0, 11, num_neighbourhoods),
    "Assaults": np.random.randint(50, 501, num_neighbourhoods),
    "Break & Enters": np.random.randint(20, 201, num_neighbourhoods),
    "Drug Arrests": np.random.randint(10, 101, num_neighbourhoods),
    "Fire Medical Calls": np.random.randint(100, 1501, num_neighbourhoods),
    "Fire Vehicle Incidents": np.random.randint(10, 501, num_neighbourhoods),
    "Fires & Fire Alarms": np.random.randint(50, 701, num_neighbourhoods),
    "Hazardous Incidents": np.random.randint(10, 201, num_neighbourhoods),
    "Murders": np.random.randint(0, 6, num_neighbourhoods),
    "Robberies": np.random.randint(10, 101, num_neighbourhoods),
    "Sexual Assaults": np.random.randint(5, 51, num_neighbourhoods),
    "Thefts": np.random.randint(5, 51, num_neighbourhoods),
    "Total Major Crime Incidents": np.random.randint(100, 1501, num_neighbourhoods),
    "Vehicle Thefts": np.random.randint(10, 301, num_neighbourhoods)
})

# Print simulated data to ensure it was properly simulated
print(simulated_data)
