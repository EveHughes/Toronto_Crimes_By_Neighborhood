#### Preamble ####
# Purpose: Downloads and saves the data from the Open Data Toronto portal
# Author: Amie Liu
# Date: 16 January 2024
# Contact: amie.liu@mail.utoronto.ca
# License: MIT
# Pre-requisites: None

#### Workspace setup ####
import pandas as pd
from io import StringIO

#### Download COVID-19 cases in Toronto data ####
import requests

# Toronto Open Data is stored in a CKAN instance. It's APIs are documented here:
# https://docs.ckan.org/en/latest/api/

# To hit our API, you'll be making requests to:
base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"

# Datasets are called "packages". Each package can contain many "resources"
# To retrieve the metadata for this package and its resources, use the package name in this page's URL:
url = base_url + "/api/3/action/package_show"
params = { "id": "wellbeing-toronto-safety"}
package = requests.get(url, params = params).json()

# To get resource data:
for idx, resource in enumerate(package["result"]["resources"]):

       # for datastore_active resources:
       if resource["datastore_active"]:
            # To get all records in CSV format:
            url = base_url + "/datastore/dump/" + resource["id"]
            resource_dump_data = requests.get(url)

            # Writing raw data to CSV
            raw_data = pd.read_csv(StringIO(resource_dump_data.text))
            raw_data.to_csv("inputs/data/raw_data/raw_data.csv")
            

