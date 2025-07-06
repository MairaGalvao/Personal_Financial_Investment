from load_couple_expenses_data import LoadCoupleExpensesData

class CoupleDataETL:

    def __init__(self):
        self.couple_expenses_data = LoadCoupleExpensesData()

    def load_csv(self):
        return self.couple_expenses_data.load_csv()

if __name__ == "__main__":
    etl = CoupleDataETL()
    df = etl.load_csv()
    print(df.head())
