import csv
from sql import  create_connection

def create_csv():
    #connect to db
    conn = create_connection("sqlite.db")

    print("Exporting data into CSV........")
    cursor = conn.cursor()
    cursor.execute("select * from Data")
    with open("data.csv", "w") as csv_file:
        #write rows into data.csv file
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)