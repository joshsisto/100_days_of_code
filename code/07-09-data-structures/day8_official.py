
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    print(', '.join(cars['Jeep']))
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    print([models[0] for models in cars.values()])
    return [models[0] for models in cars.values()]


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    grep = grep.lower()
    models = sum(cars.values(), [])  # flatten list of lists
    matching_models = [model for model in models
                       if grep in model.lower()]
    print(sorted(matching_models))
    return sorted(matching_models)


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    print({manufacturer: sorted(models) for
            manufacturer, models in cars.items()})
    return {manufacturer: sorted(models) for
            manufacturer, models in cars.items()}


get_all_jeeps()
get_first_model_each_manufacturer()
get_all_matching_models()
sort_car_models()