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
            userInput = int(input("Please enter the table number you wish to assign: "))
            self.manager.choose_table(userInput - 1)
            self.manager.show_tables()
            self.menu()
        elif self.menu_choice == '2':
            userInput = int(input("Please enter the table you wish to close out: "))
            self.manager.close_out_table(userInput - 1)
            self.manager.show_tables()
            self.menu()
        elif self.menu_choice == '3':
            self.manager.change_rate()
            self.manager.show_tables()
            self.menu()
        elif self.menu_choice == '4':
            pass
        elif self.menu_choice == '5':
            exit
        else:
            self.manager.show_tables()
            self.menu()
