import datetime
import time

class Table:
    def __init__(self, table_number, rate):
        self.table_number = table_number
        self.table_status = "Not Occupied"
        self.table_start_time = 0
        self.table_total_time =  0
        self.table_end_time = 0
        self.table_display_start_time = ' '
        self.table_display_total_time = ' '
        self.table_display_end_time = ' '
        self.rate = rate
        self.charge = 0.0


    def assign_table(self):
        if self.table_status == "Not Occupied":
            self.table_status = "Occupied"
            self.table_start_time = time.time()
            self.table_display_start_time = datetime.datetime.now().strftime('%H:%M:%S')


    def reopen_table(self):
        if self.table_status == "Occupied":
            self.table_status = "Not Occupied"
            self.table_start_time = 0
            self.table_display_start_time = ' '
            self.table_end_time = time.time()
            self.table_display_end_time = datetime.datetime.now().strftime('%H:%M:%S')
            self.table_total_time = self.table_end_time - self.table_start_time
            self.table_display_total_time = datetime.datetime.now().strftime('%H:%M:%S')
        else:
            if self.table_status == "Closed":
                self.table_status = "Not Occupied"


    def close_tables(self):
        if self.table_status == "Occupied" or self.table_status == "Not Occupied":
            self.table_status = "Closed"
            print("All tables have been shut down for the night.")


    def charge_table(self):
        self.charge = round((self.rate/60) * (self.table_total_time/60), 2)
        print(f"This person owes ${self.charge} for {self.table_display_total_time} on table {self.table_number}")
