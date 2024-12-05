import pandas as pd
import csv
from datetime import datetime
from date_entry import get_amount, get_date, get_description, get_category, get_payment_mode

class CSV:
    CSV_FILE = "Finance_tracker.csv"
    columns = ['date', 'amount', 'category', 'description', 'payment_mode']
    FORMAT = '%d-%m-%Y'

    @classmethod
    def initialize(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.columns)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description, payment_mode):
        try:
            datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Date format should be DD-MM-YYYY")

        new_entry = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description,
            'payment_mode': payment_mode
        }
        with open(cls.CSV_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.columns)
            writer.writerow(new_entry)
        print("Namaste, entry added successfully!")

    @classmethod
    def get_transaction(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df['date'] = pd.to_datetime(df['date'], format=cls.FORMAT)
        start_date = datetime.strptime(start_date, cls.FORMAT)
        end_date = datetime.strptime(end_date, cls.FORMAT)

        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the given date range.")
        else:
            print(f'Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}:')
            print(filtered_df.to_string(index=False, formatters={'date': lambda x: x.strftime(CSV.FORMAT)}))

        total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
        total_expenses = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()

        print("\nSummary:")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Net Savings: ${total_income - total_expenses:.2f}")

        return filtered_df


def add():
    CSV.initialize()
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or press enter for today's date:", allow_default=True
    )
    amount = get_amount()
    category = get_category()
    description = get_description()
    payment_mode = get_payment_mode()
    CSV.add_entry(date, amount, category, description, payment_mode)



CSV.get_transaction("02-12-2024", "06-12-2024")
