import pandas as pd
import csv
from datetime import datetime
from date_entry import get_amount, get_date, get_description, get_category, get_payment_mode

class CSV:
    CSV_FILE = "Finance_tracker.csv"
    columns = ['date', 'amount', 'category', 'description', 'payment_mode']
    
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

add()
