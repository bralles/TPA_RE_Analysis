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
