def city_functions(land, city, population=''):
    if population == '':
        return f'{city.title()}, {land.title()}'
    else:
        return f'{city.title()}, {land.title()} - population {population}'