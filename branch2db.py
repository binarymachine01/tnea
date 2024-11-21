import pandas as pd
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="con1?vex",
    database="tnea"
)

cursor = db_connection.cursor()

try:
    table_name = "branch"

    df = pd.read_excel('branch_list_2024.xlsx')

    for index, row in df.iterrows():
        insert_query = ('INSERT INTO {} (branch_code, branch_name) '
                        'VALUES ("{}", "{}")').format(table_name, row["BRANCH"], row["NAME"])
        cursor.execute(insert_query)
    db_connection.commit()

except Exception as e:
    print("e")

print("Data import successfully!")

