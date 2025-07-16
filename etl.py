from load_couple_expenses_data import LoadCoupleExpensesData
import pandas as pd

class CoupleDataETL:

    def __init__(self):
        self.couple_expenses_data = LoadCoupleExpensesData()

    def load_csv(self):
        data = self.couple_expenses_data.load_csv()
        return data

    def calculate_couple_csv_data(self, df):
        df['date'] = pd.to_datetime(df['date'])
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        return df

    def monthly_summary_2024(self, df):
        df_2024 = df[df['year'] == 2024].copy()
        income_mask = df_2024['category'].str.lower() == 'income'
        outcome_mask = df_2024['amount (₪)'] < 0
        income = df_2024[income_mask].groupby('month')['amount (₪)'].sum()
        outcome = df_2024[outcome_mask].groupby('month')['amount (₪)'].sum().abs()
        summary = pd.DataFrame({
            'income': income,
            'outcome': outcome
        }).fillna(0).reset_index()

        summary['net'] = summary['income'] - summary['outcome']
        return summary

if __name__ == "__main__":
    etl = CoupleDataETL()
    df = etl.load_csv()
    df = etl.calculate_couple_csv_data(df)
    summary_2024 = etl.monthly_summary_2024(df)
    print(summary_2024)
