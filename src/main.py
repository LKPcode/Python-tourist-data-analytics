from get import *
from sql import *
from chart import *
from create_csv import create_csv


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_menu():
    print("1. Download HTML files")
    print("2. Parse the HTML files to Download EXCEL files")
    print("3. Load the SQLite Database")
    print("4. Create CSV file")
    print("5. Open Country Chart in browser")
    print("6. Open Transportation Chart in browser")
    print("7. Open Trimester Chart in browser")
    print("8. Get total visits in the 4 year period")
    print("0. Exit")

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


#MAIN APPLICATION LOGIC

print(f"{bcolors.OKBLUE}Hello and Welcome.\nLets Begin!\nSelect what you would like to do{bcolors.ENDC}")


while True:
    print_menu()
    option = input()
    print(option)
    if option=="0": exit()
    elif option=="1":
        download_html_files()
        continue
    elif option=="2":
        download_excel_files()
        continue
    elif option=="3":
        import_into_db()
        continue
    elif option=="4":
        create_csv()
        continue
    elif option=="5":
        print(f"{bcolors.OKGREEN}How many Countries do you want to see? \nRecomended lower than 25{bcolors.ENDC}")
        limit = input()
        if not isInt(limit):
            print(f"{bcolors.FAIL}This is not an integer{bcolors.ENDC}")
            continue
        country_visits(limit)
        continue
    elif option=="6":
        transportation_visits()
        continue
    elif option=="7":
        trimino_visits()
        continue
    elif option=="8":
        total = total_visits()
        print(f"{bcolors.OKGREEN} {'Total Visits: ' + str(total)} {bcolors.ENDC}")
        continue
    else:
        print(f"{bcolors.FAIL}Input is not accepted{bcolors.ENDC}")
        continue


