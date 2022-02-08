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
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

sales = SHEET.worksheet('sales')

#data = sales.get_all_values()

#print(data)

def get_sales_data():
    """
    get sales data from user"""
    print('please enter the sales data from your last market')
    print('data should be six numbers spread with comas')
    print('Example: 32,45,32,14,70')

    data_str=input('Data here:')
    print(f'the data provided is {data_str}')


get_sales_data()