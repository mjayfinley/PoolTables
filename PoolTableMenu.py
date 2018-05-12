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
                #does not print for some reason
                print("\n \n \n \n **Invalid table number, please try again.**")
            else:
                if userInput not in range(len(self.manager.table_list)):
                    self.manager.choose_table(userInput - 1)
                    self.menu()
                elif self.manager.table_list[userInput - 1].table_status == "Occupied":
                    print("\n \n \n \n ***Table is already taken***")
                    self.manager.choose_table(userInput - 1)
                    self.menu()
                else:
                    self.manager.choose_table(userInput - 1)
                    self.manager.show_tables()
                    self.menu()
            finally:
                self.manager.show_tables()
                self.menu()


        elif self.menu_choice == '2':
            try:
                userInput = int(input("Please enter the table you wish to close out: "))
            except ValueError:
                print("\n \n \n \n **Invalid table number, please try again.**")
            else:
                if userInput not in range(len(self.manager.table_list)):
                    self.manager.close_out_table(userInput - 1)
                    self.menu()
                else:
                    self.manager.close_out_table(userInput - 1)
                    self.manager.show_tables()
                    self.menu()
            finally:
                self.manager.show_tables()
                self.menu()

        elif self.menu_choice == '3':
            try:
                userInput = int(input("Please enter the new rate: "))
            except ValueError:
                print("\n \n \n \n **Invalid rate, please try again.**")
            else:
                self.manager.change_rate(userInput)
                self.manager.show_tables()
                self.menu()
            finally:
                self.manager.show_tables()
                self.menu()

        elif self.menu_choice == '4':
            pass
        elif self.menu_choice == '5':
            exit
        else:
            self.manager.show_tables()
            self.menu()
