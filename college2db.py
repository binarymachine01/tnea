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
    table_name = "college"

    df = pd.read_excel('college_list_2024.xlsx')

    for index, row in df.iterrows():
        college_name = row['COLLEGENAME'].split(",")[0].strip()
        district = [itr.strip() for itr in row['COLLEGENAME'].split(',')[1:]][-1].strip().split(" ")[0]
        pincode = row['COLLEGENAME'].split(',')[-1].split( )[-1].strip()
        # address = ' '.join([itr.strip() for itr in row['COLLEGENAME'].split(',')[1:]][:-1] +
        #                    [[itr.strip() for itr in row['COLLEGENAME'].split(',')[1:]][-1].split(" ")[0],
        #                     [itr.strip() for itr in row['COLLEGENAME'].split(',')[1:]][-1].split(" ")[2]])
        address = ' '.join(row['COLLEGENAME'].split(',')[1:]).strip()

        insert_query = ('INSERT INTO {} (college_code, college_name, district, pincode, address) '
                        'VALUES ("{}", "{}", "{}", {}, "{}")').format(table_name, row["COLLEGECODE"],
                                                              college_name,district,pincode,address)
        # data = (
        #     row["COLLEGECODE"],
        #     college_name,
        #     district,
        #     pincode,
        #     address
        # )
        cursor.execute(insert_query)
    db_connection.commit()

except Exception as e:
    print("e")

print("Data import successfully!")

