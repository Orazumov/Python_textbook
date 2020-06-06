# Сюда помещен класс ресторан.

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Restaurant has following description:')
        print(f'Restaurant name: {self.restaurant_name}')
        print(f'Restaurant cuisine: {self.cuisine_type}')

    def open_restaurant(self):
        print('Welcome, restaurant is open!')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number):
        self.number_served += increment_number

