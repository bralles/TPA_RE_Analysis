'''
Lets capture COVID cases for plotting. Here is a site that shows you how to use the API
https://rapidapi.com/blog/covid-19-data-api-with-python-php-ruby-javascript-examples/

'''


import requests

# Endpoint that we are going to be hitting:

url = "https://covid-19-data.p.rapidapi.com/totals"

# credentials:

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "659f0d67e7msh23c12f2b1bf79d3p101746jsn01f238cd8a82"
    }

# Request for data

response = requests.request("GET", url, headers=headers)

#print:

print(response.text)
