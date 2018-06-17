cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    # l = cars['Jeep']
    # for vehicle in l:
    #     print(str(vehicle))
    # print(str(cars['Jeep']))
    return (str(cars['Jeep']))
    pass


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    first_car = []
    for k, v in cars.items():
        # print(v[0])
        first_car.append(v[0])
    print(first_car)
    return firsjt_car
    pass


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    trail_list = []
    for k, v in cars.items():
        for i in v:
            if "Trail" in i:
                trail_list.append(i)
    print(trail_list)
    return trail_list
    pass


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    pass


get_all_jeeps()
get_first_model_each_manufacturer()
get_all_matching_models()
sort_car_models()

