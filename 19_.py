'''
Lets capture COVID cases for plotting. Here is a site that shows you how to use the API
https://rapidapi.com/blog/covid-19-data-api-with-python-php-ruby-javascript-examples/

We can use this page as a guide for python syntax: 
https://www.w3schools.com/python/default.asp

'''
import mod_19

# Will use our custom function to make a call and get covid-19 data.
mod_19.get_covid_data_19("us", "2022-01-24")

