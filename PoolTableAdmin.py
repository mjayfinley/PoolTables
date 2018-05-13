import time
from datetime import datetime
from PoolTable import Table


class Admin:
    def __init__(self):
        self.table_count = 12
        self.rate = 10.00
        self.table_list = []
        self.report = []


    def open_tables(self):
        for index in range(1, self.table_count + 1):
            self.table_list.append(Table(index,self.rate))


    def change_rate(self,new_rate):
        self.rate = new_rate


    def choose_table(self,table_number):
        if table_number not in range(len(self.table_list)):
            print("\n \n \n \n ***Table does not exist, please choose a Table 1-12.***")
        else:
            self.table_list[table_number].assign_table()


    def close_out_table(self,table_number):
        if table_number not in range(len(self.table_list)):
            print("\n \n \n \n ***Table does not exist, please choose a Table 1-12.***")
        else:
            self.table_list[table_number].charge_table()
            self.table_list[table_number].reopen_table()


    def display_active_time(self):
        for table in range(len(self.table_list)):
            if self.table_list[table].table_start_time != 0:
                self.table_list[table].active_time()


    def show_tables(self):
        print('\n \n \n \n')
        print(f'The current rate is ${self.rate} per hour.')
        print('\n \n')
        print('-----------List of Tables-----------')
        print('------------------------------------')
        for table in self.table_list:
            print(f'Table {table.table_number} : {table.table_status}')
            print(f'          Time started: {table.table_display_start_time}               Time active: {table.table_display_active_time}')
        print('------------------------------------')
        print('\n \n')


    def adminInput(self):
        print("Please make a selection from the following list: ")
        print(" 1. Assign person to table")
        print(" 2. Close out table to re-open")
        print(" 3. Change hourly rate")
        print(" 4. Create report")
        print(" 5.  Quit program")
