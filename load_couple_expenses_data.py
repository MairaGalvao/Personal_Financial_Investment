import logging
import psutil
import os
import pandas as pd
from dotenv import load_dotenv

class LoadCoupleExpensesData:
    
    def load_csv(self):
        load_dotenv()
        self.data_file = os.getenv("DATA_FILE", "./data/financial_data_2024_2025.csv") 
        print(f"Loading data from {self.data_file} ...")
        df = pd.read_csv(self.data_file)
        print(f"Loaded {len(df)} rows.")
        return df
