import pandas as pd
import mysql.connector
import os


db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="con1?vex",
    database="tnea"
)
cursor = db_connection.cursor()


def list_files(folder_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

folder_path = os.path.join(os.getcwd(), 'xlsx', 'with_community')
files = list_files(folder_path)



try:
    table_name = "candidate_allotment"
    for file in files:

        year = os.path.basename(file).split(".")[0].split("_")[0]
        rd = os.path.basename(file).split(".")[0].split("_")[1]

        print(year,rd)

        excel_file = file
        df = pd.read_excel(excel_file)
        for index, row in df.iterrows():
            insert_query = f"""
            INSERT INTO {table_name} (
                s_no, aggr_mark, general_rank, community_rank, community,
                college_code, branch_code, allotted_category, year, round
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                row["SNO"],
                row["AGGRMARK"],
                row["GENERALRANK"],
                row["COMMUNITYRANK"],
                row["COMMUNITY"],
                row["COLLEGECODE"],
                row["BRANCHCODE"],
                row["ALLOTTEDCATEGORY"],
                year, rd
            )
            cursor.execute(insert_query, data)

    db_connection.commit()

except Exception as e:
    print("e")

print("Data import successfully!")
