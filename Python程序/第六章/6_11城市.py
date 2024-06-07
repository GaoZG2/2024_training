cities = {'hz':
            {
                'country': ' China',
                'population': 5_000_000,
                'fact': 'ZUST is located here'
            },
          'wh':
            {
                'country': ' China',
                'population': 5_000_000,
                'fact': 'HUST is located here'
            },
          'bj':
            {
                'country': ' China',
                'population': 10_000_000,
                'fact': 'PUST is located here'
            }  
        }
for city, information in cities.items():
    print(city, ': ', information)