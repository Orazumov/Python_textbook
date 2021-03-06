class User():

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'User information: name: {self.first_name} surname: {self.last_name} email: {self.email} age: {self.age}')

    def greet_user(self):
        print('Hello, ' + self.first_name.title() + ' ' + self.last_name.title() + '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():

    def __init__(self, privileges=['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей']):
        self.privileges = privileges

    def show_privileges(self):
        print('User privileges:')
        for priv in self.privileges:
            print(f'- {priv}')


class Admin(User):

    def __init__(self, first_name, last_name, email, age):
        super().__init__(first_name, last_name, email, age)
        self.privileges = Privileges()
