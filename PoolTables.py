import time
import datetime

tables = []
table_status = "Occupied"

#class creation for Table
class Table:
    def __init__(self,table_number):
        self.table_number = table_number
        self.table_status = "Not Occupied"
        self.table_start_time = ' '
        self.table_active_time = ' '
        self.table_end_time = ' '
        self.table_display_start_time = ' '
        self.table_display_active_time = ' '
        self.table_display_end_time = ' '
        self.rate = 0.0

def open_tables():
    table_setup = ['Table 1','Table 2','Table 3','Table 4','Table 5','Table 6','Table 7', 'Table 8', 'Table 9','Table 10','Table 11','Table 12']
    num_of_tables = 0
    while num_of_tables < len(table_setup):
        tables.append(Table(table_setup[num_of_tables]))
        num_of_tables += 1

def assign_table():
    #try statement?
    userInput = int(input("Please enter table number you wish to assign: "))
    table = userInput - 1
    if tables[table].table_status == "Not Occupied":
        tables[table].table_status = "Occupied"
        tables[table].table_start_time = datetime.datetime.now()
        tables[table].table_display_start_time = tables[table].table_start_time.strftime('%H:%M')
    else:
        print("\n \n \n ##Table is currently Occupied, please choose another table##")
    return show_tables()

def active_time():
    pass

def close_table():
    userInput = int(input("Please enter the table you would like to close: "))
    table = userInput - 1
    if tables[table].table_status == "Occupied":
        tables[table].table_status = "Not Occupied"
        tables[table].table_start_time = ' '
        tables[table].table_display_start_time = ' '
        tables[table].table_end_time = datetime.datetime.now()
        tables[table].table_display_end_time = tables[table].table_end_time.strftime('%H:%M')

    else:
        print("\n \n \n ##Table is already open!##")
    return show_tables()

def change_rate():
    pass

def email_report():
    pass

def show_tables():
    print('\n \n \n \n')
    print('-----------List of Tables-----------')
    print('------------------------------------')
    print(f'Table 1 : {tables[0].table_status}')
    print(f'          Time started: {tables[0].table_display_start_time}        Time active:  {tables[0].table_display_active_time}')
    print(f'Table 2 : {tables[1].table_status}')
    print(f'          Time started: {tables[1].table_display_start_time}        Time active:  {tables[1].table_display_active_time}')
    print(f'Table 3 : {tables[2].table_status}')
    print(f'          Time started: {tables[2].table_display_start_time}       Time active:  {tables[2].table_display_active_time}')
    print(f'Table 4 : {tables[3].table_status}')
    print(f'          Time started: {tables[3].table_display_start_time}       Time active:  {tables[3].table_display_active_time}')
    print(f'Table 5 : {tables[4].table_status}')
    print(f'          Time started: {tables[4].table_display_start_time}       Time active:  {tables[4].table_display_active_time}')
    print(f'Table 6 : {tables[5].table_status}')
    print(f'          Time started: {tables[5].table_display_start_time}       Time active:  {tables[5].table_display_active_time}')
    print(f'Table 7 : {tables[6].table_status}')
    print(f'          Time started: {tables[6].table_display_start_time}       Time active:  {tables[6].table_display_active_time}')
    print(f'Table 8 : {tables[7].table_status}')
    print(f'          Time started: {tables[7].table_display_start_time}       Time active:  {tables[7].table_display_active_time}')
    print(f'Table 9 : {tables[8].table_status}')
    print(f'          Time started: {tables[8].table_display_start_time}       Time active:  {tables[8].table_display_active_time}')
    print(f'Table 10: {tables[9].table_status}')
    print(f'          Time started: {tables[9].table_display_start_time}       Time active:  {tables[9].table_display_active_time}')
    print(f'Table 11: {tables[10].table_status}')
    print(f'          Time started: {tables[10].table_display_start_time}      Time active:  {tables[10].table_display_active_time}')
    print(f'Table 12: {tables[11].table_status}')
    print(f'          Time started: {tables[11].table_display_start_time}      Time active:  {tables[11].table_display_active_time}')
    print('------------------------------------')
    print('\n \n')
    adminInput()

def adminInput():
    print("Please make a selection from the following list: ")
    print("    1. Assign person to Table")
    print("    2. Close out table")
    print("    3. Change hourly rate")
    print("    4. Email report")
    print("    5. Quit Program")
    action = input()

    if action == '1':
        assign_table()
    elif action == '2':
        close_table()
    elif action == '3':
        pass
    elif action == '4':
        pass
    elif action == '5':
        exit
        print("Please press return to confirm quit.")
    else:
        show_tables()

open_tables()
show_tables()

print(input())
