import logging
import psutil
import os
import pandas as pd

class LoadCoupleExpensesData:
    
    def load_csv(self):
        self.data_file = os.getenv("DATA_FILE", "./data/financial_data_couple_shekels.csv") 
        print(f"Loading data from {self.data_file} ...")
        df = pd.read_csv(self.data_file)
        print(f"Loaded {len(df)} rows.")
        return df
