#### Preamble ####
# Purpose: Downloads and saves the data from opendata Toronto
# Author: Bruce Zhang
# Date: 23 September 2024
# Contact: brucejc.zhang@mail.utoronto.ca
# License: MIT
# Pre-requisites: None
# Any other information needed? None


#### Workspace setup ####
library(opendatatoronto)
library(tidyverse)

#### Download data ####
# get package
package <- show_package("7e038ff9-b616-4070-9753-6f493b2cdbb0")
package

#### Save data ####
# change the_raw_data to whatever name you assigned when you downloaded it.
write_csv(x = raw_data, file = "data/raw_data/raw_data.csv") 

         
