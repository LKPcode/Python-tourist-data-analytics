import sqlite3
import pandas



def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file ,  timeout=10)
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    sql ='''CREATE TABLE IF NOT EXISTS "Data" (
                "id"	INTEGER,
                "country"	TEXT,
                "plane"	INTEGER NOT NULL DEFAULT 0,
                "train"	INTEGER NOT NULL DEFAULT 0,
                "boat"	INTEGER NOT NULL DEFAULT 0,
                "car"	REAL NOT NULL DEFAULT 0,
                "total"	INTEGER NOT NULL,
                "month"	TEXT NOT NULL,
                "year"	INTEGER,
                PRIMARY KEY("id" AUTOINCREMENT)
            );'''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def create_row(conn, project):
    sql = ''' INSERT INTO Data (country, plane, train, boat, car, total, month, year)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid

def import_into_db():
    conn = create_connection("./sqlite.db")
    create_table(conn)
    month_name = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    
    #import data into the Database
    for year in range(2011,2015):
        for month in range(0,12):
            #get excel data frame
            data = pandas.read_excel("./excel/" + str(year) + "/4/1.xls", sheet_name=month ,  keep_default_na=True)
            test_df = data.iloc[6: , 1:]
            #for every row of the dataframe create a row in the Data table of SQLite
            for index, row in test_df.iterrows():
                print(row["Unnamed: 1"] , row["Unnamed: 2"], row["Unnamed: 3"],row["Unnamed: 4"],row["Unnamed: 5"],  row["Unnamed: 6"])
                #ignore null values
                if pandas.isnull(row["Unnamed: 1"]): continue
                if pandas.isnull(row["Unnamed: 3"]) or pandas.isnull(row["Unnamed: 2"]) or pandas.isnull(row["Unnamed: 4"]) or pandas.isnull(row["Unnamed: 5"]): continue
                #create database row
                create_row(conn , (row["Unnamed: 1"] , int(float(row["Unnamed: 2"])), int(float(row["Unnamed: 3"])),
                                        int(float(row["Unnamed: 4"])), int(float(row["Unnamed: 5"])),  int(float(row["Unnamed: 6"])), month_name[month], year))
                #next sheet
                if row["Unnamed: 1"]=='ΓΕΝΙΚΟ ΣΥΝΟΛΟ': break

    #make imports permanent (save)
    conn.commit()
