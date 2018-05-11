import time
import datetime
from string import Template

tables = []

#class creation for Table
class Table:
    def __init__(self,table_number):
        self.table_number = table_number
        self.table_status = "Not Occupied"
        self.table_start_time = ' '
        self.table_active_time = ' '
        self.table_end_time = ' '
        self.table_display_start_time = '00:00'
        self.table_display_active_time = ' '
        self.table_display_end_time = '00:00'
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
        tables[table].table_display_active_time = "00:00"
    else:
        print("\n \n \n ##Table is currently Occupied, please choose another table##")
    return show_tables()

class DeltaTemplate(Template):
    delimiter = '%'

def strfdelta(tdelta,fmt):
    d = {"D": tdelta.days}
    hours, rem = divmod(tdelta.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    d["H"] = '{:02d}'.format(hours)
    d["M"] = '{:02d}'.format(minutes)
    d["S"] = '{:02d}'.format(seconds)
    t = DeltaTemplate(fmt)
    return t.substitute(**d)

def active_time():
    current_time = datetime.datetime.now()
    for i in range(len(tables)):
        if tables[i].table_display_active_time == "00:00":
            tables[i].table_active_time = current_time - datetime.datetime.strptime(tables[i].table_display_start_time, '%H:%M')
            tables[i].table_display_active_time = strfdelta(tables[i].table_active_time, '%H:%M')
        else:
            tables[i].table_display_active_time = ' '
    return show_tables()


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
    for table in range(len(tables)):
        print(f'Table {table + 1} : {tables[table].table_status}')
        print(f'          Time started: {tables[table].table_display_start_time}' + f'      ' + f'Time active:  {tables[table].table_display_active_time}')
    print('------------------------------------')
    print('\n \n')
    adminInput()

def adminInput():
    print("Please make a selection from the following list: ")
    print("    1. Assign person to Table")
    print("    2. Close out table")
    print("    3. Change hourly rate")
    print("    4. Email report")
    print("    5. Refresh Tables")
    print("    6. Quit Program")
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
        active_time()
    elif action == '6':
        exit
        print("Please press return to confirm quit.")
    else:
        show_tables()

open_tables()
show_tables()

print(input())
