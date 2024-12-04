from datetime import datetime

date_format = "%d-%m-%Y"
categories = {'I': "Income", "E":"Expense"}
payment_modes = ['cash', 'UPI', 'credit card']

def get_date(prompt,allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format please enter the date in dd-MM-yyyy format")
        return get_date(prompt,allow_default)


def get_amount():
    try:
        amount = float(input("Enter the amount: ")) 
        if amount <= 0:  
            raise ValueError("Invalid amount")
    except ValueError as e:
        print(e)
        return get_amount()
    
def get_category():
    category = input("Enter the category: ( 'I' for Income or 'E' for Expense): ").upper()
    if category in categories:
        return categories[category]
    
    print("invalid category")
    return get_category()

def get_description():
    description = input("Enter a description: ")
    return description


def get_payment_mode():
    payment_mode = input("Enter the payment mode (e.g., cash, UPI, credit card): ")
    if payment_mode in payment_modes:
        return payment_modes
    print("invalid payment mode")
    return get_payment_mode()