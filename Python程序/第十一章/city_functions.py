def city_country(city, country, population=-1):
    if population == -1:
        return f'{city.title()} {country.title()}'
    else:
        return f'{city.title()} {country.title()} -population {population}'