'''

This file will contain all custom functions. All functions will end with suffix _19 so that we know it is 
one that we created for us.

'''
import requests
from requests.exceptions import HTTPError

def get_covid_data_19(country_name, date):
    '''
    This function gets COVID 19 data via rapid API. This takes two parameters: 
    Country Name (string) and Date (YYYY-MM-DD)
    API info and config: https://rapidapi.com/Gramzivi/api/covid-19-data/

    '''
    import json
    c = country_name
    d = date
    # Endpoint that we are going to be hitting:
    url = "https://covid-19-data.p.rapidapi.com/report/country/name"

    querystring = {"name":c,"date":d, "format":"json"}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "659f0d67e7msh23c12f2b1bf79d3p101746jsn01f238cd8a82"
        }

    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        response.raise_for_status()
        r = response.json()
    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
    except Exception as err:
        print(f'Other erro occured: {err}')
    

    print("Printing the content of the response: ")
    for key, value in r[0].items():
        print(key, ":", value)
    
 
    
    

    '''
    #TODO 
    This needs to be recode in order to strip out the following sample response: 

    [1 item
    0:{5 items
    "country":"Italy"
    "provinces":[1 item
    0:{5 items
    "province":"Italy"
    "confirmed":110574
    "recovered":16847
    "deaths":13155
    "active":80572
    }
    ]
    "latitude":41.87194
    "longitude":12.56738
    "date":"2020-04-01"
    }
    ]

    #clean it
    remove_symbols = ["[", "]", "{", "}"]
    for i in remove_symbols :
        json_data = json_data.replace(i, "")

    #split string
    split_str = json_data.split(",")

    #data types as variables
    confirmed = split_str[0]
    recovered = split_str[1]
    critical  = split_str[2]
    deaths = split_str[3]

    #pretty print
    print("{}\n{}\n{}\n{}".format(confirmed, recovered, critical, deaths).replace('"', ""))
    '''