from PoolTableAdmin import Admin

class Menu:
    def __init__(self):
        self.manager = Admin()
        self.manager.open_tables()
        self.menu_choice = ' '
    def menu(self):
        self.manager.show_tables()
        self.manager.adminInput()
        self.menu_choice = input()


        if self.menu_choice == '1':
            try:
                userInput = int(input("Please enter the table number you wish to assign: "))
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
                userInput = int(input("Please enter the table you wish to close out: "))
            except ValueError:
                print("\n \n \n \n \n \n***Please enter a number 1-12.***")
            else:
                if userInput not in range(len(self.manager.table_list)):
                    self.manager.close_out_table(userInput - 1)
                    self.manager.append_report(userInput - 1)
                    self.menu()
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
            exit

        else:
            print("\n \n ***Please select from the list***")
            self.manager.display_active_time()
            self.menu()
