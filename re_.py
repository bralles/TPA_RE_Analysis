'''
OK. Getting serious now. 

The idea is to build a program that receives zip codes as inputs and gives you average price per square feet for that area.
We will then create a database to store info so that we can build historical data that we can use to lay on a chart.

'''

# Instantiating the ZillowWrapper from PyZillow

from pyzillow.pyzillow import ZillowWrapper

# We need a Zillow Web Services ID (ZWSID) by going to Zillow and applying for one. I am going to apply for one since 
# I already have an account and past the API key here. As a developer, you are not supposed to paste it here as this 
# can obtained by hackers. But its ok, because we are not dealing with sensitive data and we are just playing.