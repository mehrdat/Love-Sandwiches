import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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


def get_sales_data():
    while True: 
        """
        get sales data from user
        """
        print('please enter the sales data from your last market')
        print('data should be six numbers spread with comas')
        print('Example: 32,45,32,14,70')

        data_str = input('Data here:')
        sales_data = data_str.split(',')
        if (validate_data(sales_data)):
            print('data is valid')
            break
    return sales_data
    


def validate_data(values):
    """
    to Validate the data prepared for the validation
    """
    
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(f'exactly 6 value required you prepared {len(values)}')

    except ValueError as e:
        print(f'inavalid data : {e} please try again')
        return False
    
    return True
   
def update_sales_worksheet(data):
    """ update the data in sales worksheet"""
    print('Updating the saes worksheet...\n')
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print('updated succesfully\n')

def calculate_surplus_data(sales_row):
    """ stock - sales= surplus"""
    print('calculating surplus ...\n')
    stock=SHEET.worksheet('stock').get_all_values()
    #pprint(stock)
    stock_row=stock[-1]
    
    surplus_data=[]
    for stock,sales in zip(stock_row,sales_row):
        surplus=int(stock)-sales
        surplus_data.append(surplus)
    
    return surplus_data
    

def main():
    """
    the main function
    """
    data=get_sales_data()
    sales_data=[int(value) for value in data]
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)

print('welcome to the sandwich sheet program')
main()