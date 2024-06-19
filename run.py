import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

""""
Test connection
sales = SHEET.worksheet('sales')
data = sales.get_all_values()
print(data)
"""

def get_sales_data():
    """
    Get sales figures input from user
    """
    print("Enter sales data")
    print("Data should be six figures")
    print("Example: 20,30,40,50,60,70\n")

    data_str = input("Enter your data here: ")
    sales_data = data_str.split(",")

    validate_data(sales_data)

def validate_data(values):
    """
    inside try method convert all values to integer
    Raise error if value cannot be converted to integer
    or the number of values are not exactly 6
    """
    
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data type {e}, please try again \n")

    print(values)

get_sales_data()