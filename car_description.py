def car_description(vendor: str, model: str, **kwargs) -> dict:
    '''
    This function returns dict with car description
    :param kwargs: any number of params
    :return: dictionary
    '''

    car_desc = {}
    car_desc['vendor'] = vendor
    car_desc['model'] = model

    for key, value in kwargs.items():
        car_desc[key] = value

    return car_desc