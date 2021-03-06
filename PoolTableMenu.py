from PoolTableAdmin import Admin


class Menu:
    def __init__(self):
        self.manager = Admin()
        self.manager.open_tables()
        self.menu_choice = ' '

    def menu(self):

        while self.menu_choice != '4':
            self.manager.show_tables()
            self.manager.adminInput()
            self.menu_choice = input()

            if self.menu_choice == '1':
                try:
                    userInput = int(
                        input("Please enter the table number you wish to assign: "))
                except ValueError:
                    print("\n \n ***Please enter a number 1-12.***")
                else:
                    if userInput not in range(len(self.manager.table_list)):
                        self.manager.choose_table(userInput - 1)
                        self.menu()
                    elif self.manager.table_list[userInput - 1].table_status == "Occupied":
                        print("\n \n ***Table is already taken***")
                        self.manager.choose_table(userInput - 1)
                        self.menu()
                    else:
                        self.manager.choose_table(userInput - 1)
                        self.manager.display_active_time()
                        self.menu()
                finally:
                    self.manager.display_active_time()
                    self.menu()

            elif self.menu_choice == '2':
                try:
                    userInput = int(
                        input("Please enter the table you wish to close out: "))
                except ValueError:
                    print("\n \n \n \n \n \n***Please enter a number 1-12.***")
                else:
                    if userInput not in range(len(self.manager.table_list)):
                        self.manager.close_out_table(userInput - 1)
                        self.manager.append_report(userInput - 1)
                        self.menu()
                    elif self.manager.table_list[userInput - 1].table_status == "Not Occupied":
                        print("\n \n ***Table is Not Occupied***")
                    else:
                        self.manager.close_out_table(userInput - 1)
                        self.manager.append_report(userInput - 1)
                        self.manager.display_active_time()
                        self.menu()
                finally:
                    self.manager.display_active_time()
                    self.menu()

            elif self.menu_choice == '3':
                try:
                    userInput = int(input("Please enter the new rate: "))
                except ValueError:
                    print("\n \n ***Please enter a valid amount***")
                else:
                    self.manager.change_rate(userInput)
                    self.manager.display_active_time()
                    self.menu()
                finally:
                    self.manager.display_active_time()
                    self.menu()
            elif self.menu_choice == '4':
                print("\n \n ***Goodbye***")
                for table in self.manager.table_list:
                    if self.manager.table_list[table.table_number - 1].table_status == "Occupied":
                        self.manager.close_out_table(
                            self.manager.table_list[table.table_number - 1].table_number)
                        self.manager.append_report(
                            self.manager.table_list[table.table_number - 1].table_number)
            else:
                print("\n \n ***Please select from the list***")
                self.manager.display_active_time()
                self.menu()
