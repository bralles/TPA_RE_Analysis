# Our first python file. 

import requests

url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"

querystring = {"location":"33625","home_type":"Houses"}

headers = {
    'x-rapidapi-host': "zillow-com1.p.rapidapi.com",
    'x-rapidapi-key': "659f0d67e7msh23c12f2b1bf79d3p101746jsn01f238cd8a82"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)