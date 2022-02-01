'''

This file will contain all custom functions. All functions will end with suffix _19 so that we know it is 
one that we created for us.

'''
import requests
import json

def get_covid_data_19(country_code, date):
    '''
    This function gets COVID 19 data via rapid API. This takes two parameters: 
    Country Name (string) and Date (YYYY-MM-DD)
    API info and config: https://rapidapi.com/Gramzivi/api/covid-19-data/

    '''
    c = country_code
    d = date
    # Endpoint that we are going to be hitting:
    url = "https://covid-19-data.p.rapidapi.com/report/country/code"

    querystring = {"code" : c, "date" : d}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "659f0d67e7msh23c12f2b1bf79d3p101746jsn01f238cd8a82"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = response.json()
    
    data = []
    for response in json_data:
        data.append ({
            'confirmed' : response.get('confirmed'),
            'recovered' : response.get('recovered'),
            'deaths' : response.get('deaths'),
            'active' : response.get('active'),
            'date' : response.get('date'),
        })

    print(data)
    print(json_data)