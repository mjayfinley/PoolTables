import datetime
from time import strftime

table_setup = ['Table 1','Table 2','Table 3','Table 4','Table 5','Table 6','Table 7', 'Table 8', 'Table 9','Table 10','Table 11','Table 12']
tables = []
table_status = "Occupied"
start_time = datetime.datetime.now()
current_time = datetime.datetime.now()
active_time = datetime.datetime.now()
end_time = datetime.datetime.now()
rate = 10.00

#class creation for Table
class Table:
    def __init__(self,table_number):
        self.table_number = table_number
        self.table_status = "Not Occupied"
        self.table_start_time = []
        self.table_active_time = []
        self.rate = []

def open_tables():
    num_of_tables = 0
    while num_of_tables < len(table_setup):
        tables.append(Table(table_setup[num_of_tables]))
        num_of_tables += 1

def assign_table():
    userInput = int(input("Please enter table number you wish to assign: "))
    if tables[userInput-1].table_status == table_status:
        print("\n \n ##Table is already taken.##")
    elif userInput == 1:
        tables[0].table_status = table_status
        tables[0].table_start_time.append(start_time())
        #tables[0].table_active_time.append(active_time())
    elif userInput == 2:
        tables[1].table_status = table_status
    elif userInput == 3:
        tables[2].table_status = table_status
    elif userInput == 4:
        tables[3].table_status = table_status
    elif userInput == 5:
        tables[4].table_status = table_status
    elif userInput == 6:
        tables[5].table_status = table_status
    elif userInput == 7:
        tables[6].table_status = table_status
    elif userInput == 8:
        tables[7].table_status = table_status
    elif userInput == 9:
        tables[8].table_status = table_status
    elif userInput == 10:
        tables[9].table_status = table_status
    elif userInput == 11:
        tables[10].table_status = table_status
    elif userInput == 12:
        tables[11].table_status = table_status
    else:
        print("\n \n ##Table does not exist. Please choose number 1-12.##")
    return show_tables()

def start_time():
    start_time = datetime.datetime.now()
    return start_time

#def active_time():
#    current_time = datetime.datetime.now()
#    active_time = (current_time - tables[0].table_start_time).total_seconds()
#    return active_time

def end_time():
    now = datetime.datetime.now()
    end_time = datetime.datetime.strptime(now)

def close_table():
    pass

def change_rate():
    pass

def email_report():
    pass

def show_tables():
    print('\n \n')
    print('-----------List of Tables-----------')
    print('------------------------------------')
    print(f'Table 1 : {tables[0].table_status}')
    print(f'          Time started: {tables[0].table_start_time}')
    #print(f'          Time active: {tables[0].table_active_time}')
    print(f'Table 2 : {tables[1].table_status}')
    print(f'Table 3 : {tables[2].table_status}')
    print(f'Table 4 : {tables[3].table_status}')
    print(f'Table 5 : {tables[4].table_status}')
    print(f'Table 6 : {tables[5].table_status}')
    print(f'Table 7 : {tables[6].table_status}')
    print(f'Table 8 : {tables[7].table_status}')
    print(f'Table 9 : {tables[8].table_status}')
    print(f'Table 10: {tables[9].table_status}')
    print(f'Table 11: {tables[10].table_status}')
    print(f'Table 12: {tables[11].table_status}')
    print('------------------------------------')
    print('\n \n')
    adminInput()

def adminInput():
    print("Please make a selection from the following list: ")
    print("    1. Assign person to Table")
    print("    3. Close out table")
    print("    4. Change hourly rate")
    print("    5. Email report")
    print("    6. Quit Program")
    action = input()

    if action == '1':
        assign_table()
    elif action == '2':
        start_time()
    elif action == '3':
        pass
    elif action == '4':
        pass
    elif action == '5':
        pass
    elif action == '6':
        exit
        print("Please press return to confirm quit.")
    else:
        show_tables()

open_tables()
show_tables()

print(input())
