'''

This file will contain all custom functions. All functions will end with suffix _19 so that we know it is 
one that we created for us.

'''
import requests

def get_covid_data_19():
    '''
    This function gets COVID 19 data via rapid API. 

    '''
    # Endpoint that we are going to be hitting:
    url = "https://covid-19-data.p.rapidapi.com/totals"
    # credentials:
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "659f0d67e7msh23c12f2b1bf79d3p101746jsn01f238cd8a82"
        }
    # Request for data
    response = requests.request("GET", url, headers=headers)
    json_data = response.text

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
