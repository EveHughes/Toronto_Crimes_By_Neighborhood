#### Preamble ####
# Purpose: Tests the data
# Author: Kevin Lin
# Date: 23 September 2024
# Contact: kevin.lin@mail.utoronto.ca
# License: MIT

import unittest
import pandas as pd
import matplotlib.pyplot as plt

class TestCrimeData(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Load both datasets
        cls.simulated_data = pd.read_csv("data/raw_data/raw_data.csv")
        cls.analysis_data = pd.read_csv("data/analysis_data/analysis_data.csv")
    
    # Simulated data tests
    def test_simulated_data_not_empty(self):
        self.assertFalse(self.simulated_data.empty, "Simulated data is empty.")
    
    def test_simulated_data_no_missing(self):
        missing = self.simulated_data.isnull().sum().sum()
        self.assertEqual(missing, 0, f"Simulated data has {missing} missing values.")
    
    def test_simulated_data_no_duplicates(self):
        duplicates = self.simulated_data.duplicated().sum()
        self.assertEqual(duplicates, 0, f"Simulated data has {duplicates} duplicate rows.")
    
    def test_simulated_data_unique_counts(self):
        unique_counts = self.simulated_data.nunique()
        self.assertTrue((unique_counts > 1).all(), "Some columns in simulated_data have only 1 unique value.")

    # Analysis data tests
    def test_analysis_data_not_empty(self):
        self.assertFalse(self.analysis_data.empty, "Analysis data is empty.")
    
    def test_analysis_data_no_missing(self):
        missing = self.analysis_data.isnull().sum().sum()
        self.assertEqual(missing, 0, f"Analysis data has {missing} missing values.")
    
    def test_analysis_data_no_duplicates(self):
        duplicates = self.analysis_data.duplicated().sum()
        self.assertEqual(duplicates, 0, f"Analysis data has {duplicates} duplicate rows.")
    
    def test_analysis_data_unique_counts(self):
        unique_counts = self.analysis_data.nunique()
        self.assertTrue((unique_counts > 1).all(), "Some columns in analysis_data have only 1 unique value.")

# Optional visualization (run separately from tests)
def visualize_analysis_data():
    df = pd.read_csv("data/analysis_data/analysis_data.csv")
    plt.figure(figsize=(10, 6))
    plt.xticks(rotation=90)
    plt.scatter(df["neighbourhood"], df["total_major_crime_incidents"])
    plt.title("Total Major Crime Incidents by Neighbourhood")
    plt.xlabel("Neighbourhood")
    plt.ylabel("Total Major Crime Incidents")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    unittest.main()
