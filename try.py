import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = "New_Tracker.csv"
    columns = ['date', 'amount', 'category', 'description', 'payment_mode']

    @classmethod
    def initialize(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.columns)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls):
        # Ask the user for input
        try:
            date = input("Enter the date (DD-MM-YYYY): ")
            datetime.strptime(date, "%d-%m-%Y")  # Validate the date format
        except ValueError:
            raise ValueError("Date format should be DD-MM-YYYY")
        
        try:
            amount = float(input("Enter the amount: "))  # Ensure the amount is numeric
        except ValueError:
            raise ValueError("Amount must be a number")

        category = input("Enter the category (e.g., groceries, rent, etc.): ")
        description = input("Enter a description: ")
        payment_mode = input("Enter the payment mode (e.g., cash, UPI, credit card): ")

        # Create the new entry
        new_entry = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description,
            'payment_mode': payment_mode
        }

        # Append the new entry to the CSV file
        with open(cls.CSV_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.columns)
            writer.writerow(new_entry)

        print("Namaste! Entry added successfully:", new_entry)

    @classmethod
    def view_record(cls):
        try:
            df = pd.read_csv(cls.CSV_FILE)
            if df.empty:
                print("No records found in the tracker.")
            else:
                print("Here are the records in your finance tracker:")
                print(df.to_string(index=False))
        except FileNotFoundError:
            print("No records found. Please initialize the tracker first.")


# Initialize the CSV file
CSV.initialize()

while True:
    print("finace_tracker")
    print("1. Add entry")
    print("2. view_records")
    print("3. Exit")
    choice = int(input("Enter your choise (1/2/3): "))

    if choice==1:
        CSV.add_entry()
    elif choice==2:
        CSV.view_record()
    elif choice==3:
        print("Thank you for using the Finance Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

# Interactive entry
# CSV.add_entry()
