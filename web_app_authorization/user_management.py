import datetime

class User:
    data_base = None
    def __init__(self):
        self.user_id = None
        self.user_name = None
        self.password = None
        self.date_of_registration = None
        
        self.notes = []

    def __str__(self):
        N_of_spaces = 50
        frame = '+' + '-' * N_of_spaces + '+\n'
        user_info = f'| User Name: {self.user_name}{" " * (37 - len(self.user_name))} |\n'
        reg_info = f'| Registration Date: {self.date_of_registration}{" " * (29 - len(str(self.date_of_registration)))} |\n'
        return frame + user_info + reg_info + frame
    
    


def user_print_test():
    user = User()
    user.user_name = 'john'
    user.date_of_registration = datetime.datetime.now()
    print(user)

user_print_test()