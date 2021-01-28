#!/usr/bin/python3

from pprint import pprint as pp

country_to_capital = {'United Kingdom' : 'London',
                      'Brazil' : 'Brazilia',
                       'Morrocco': 'Rabbat',
                       'Sweden' : ' Stockholm'}

capital_to_country= {capital: country for country, capital in country_to_capital.items()}

pp(capital_to_country)
