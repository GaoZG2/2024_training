def make_car(brand, model, **args):
    args['brand'] = brand
    args['model'] = model
    return args

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)