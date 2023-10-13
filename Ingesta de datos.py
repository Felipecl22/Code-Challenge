# Ingesta de datos 24 hrs.

import pyodbc
import schedule
import time

# Define your SQL Server connection parameters
server = 'DESKTOP-TKNQKG7\SQLEXPRESS'
database = 'Ventas Minoristas'
trusted_connection = 'yes'  # For Windows authentication

def data_ingestion():
    # Establish the database connection
    conn = pyodbc.connect(
        f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'
    )

    # Define the data to be inserted with example values
    invoice_no = 'INV12345'
    stock_code = 'ABC123'
    description = 'Sample Product'
    quantity = 20
    invoice_date = '2023-10-13'
    unit_price = 9.99
    customer_id = 'CUST567'
    country = 'USA'

    # SQL query to insert data into your table
    sql_query = f"""
    INSERT INTO YourTable (Invoice_No, Stock_Code, Description, Quantity, Invoice_Date, UnitPrice, Customer_ID, Country)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """

    # Execute the SQL query
    cursor = conn.cursor()
    cursor.execute(sql_query, (invoice_no, stock_code, description, quantity, invoice_date, unit_price, customer_id, country))
    conn.commit()

    # Close the database connection
    conn.close()

# Schedule the data ingestion to run every 24 hours
schedule.every(24).hours.do(data_ingestion)

while True:
    schedule.run_pending()
    time.sleep(1)

