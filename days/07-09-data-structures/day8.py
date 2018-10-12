cars = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    return ", ".join(cars["Jeep"])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [models[0] for models in cars.values()]


def get_all_matching_models(cars=cars, grep="trail"):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    all_models = []
    for models in cars.values():
        all_models += models
    grep = grep.lower()
    matching = []
    for model in all_models:
        if grep in model.lower():
            matching.append(model)
    matching.sort()
    return matching


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    sorted_cars = {}
    for brand, models in cars.items():
        models.sort()
        sorted_cars[brand] = models
    return sorted_cars


# Tests


def test_get_all_jeeps():
    expected = "Grand Cherokee, Cherokee, Trailhawk, Trackhawk"
    actual = get_all_jeeps()
    assert type(actual) == str
    assert actual == expected


def test_get_first_model_each_manufacturer():
    actual = get_first_model_each_manufacturer()
    expected = ["Falcon", "Commodore", "Maxima", "Civic", "Grand Cherokee"]
    assert actual == expected


def test_get_all_matching_models():
    expected = ["Trailblazer", "Trailhawk"]
    assert get_all_matching_models() == expected
    expected = ["Accord", "Commodore", "Falcon"]
    assert get_all_matching_models(grep="CO") == expected


def test_sort_dict_alphabetically():
    actual = sort_car_models()
    # Order of keys should not matter, two dicts are equal if they have the
    # same keys and the same values.
    # The car models (values) need to be sorted here though
    expected = {
        "Ford": ["Fairlane", "Falcon", "Festiva", "Focus"],
        "Holden": ["Barina", "Captiva", "Commodore", "Trailblazer"],
        "Honda": ["Accord", "Civic", "Jazz", "Odyssey"],
        "Jeep": ["Cherokee", "Grand Cherokee", "Trackhawk", "Trailhawk"],
        "Nissan": ["350Z", "Maxima", "Navara", "Pulsar"],
    }
    assert actual == expected


if __name__ == "__main__":
    test_get_all_jeeps()
    test_get_all_matching_models()
    test_get_first_model_each_manufacturer()
    test_sort_dict_alphabetically()
    print("Passed tests!")

