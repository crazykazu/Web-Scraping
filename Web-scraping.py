# Importing all the stuff that I need for the webscrapping
import requests
from bs4 import BeautifulSoup


# Gets the list of all the tickers that you want to look up
def getting_list():
    # Making the main list that it will return
    the_list = []
    # Runs a while loop so people can enter in as many tickers as they want
    while True:
        # Asking for input
        response = input("Enter in the exact ticker symbol of the company (If no more than just hit enter): ")
        # If the input was not blank then append to list of tickers
        if response != "":
            the_list.append(response)
        # If it was blank then break out of while loop
        else:
            return the_list


# Will get the change of the stock while the market is open (NOT AFTER HOURS CHANGE) and takes in the ticker
def day_change(ticker):
    # Gets the website
    response = requests.get('https://www.marketwatch.com/investing/stock/' + ticker)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Webscraping to find the exact number that I want and I had a bit of trouble with this because
    # the percentage change and then like the change in amount have the same class so I had to make it
    # so I get a list and then return the second item because that is the item that I want
    all_change = soup.find(class_='remove-last-border').find_all(class_='table__cell')
    all_percents = []
    # Looping through everything to get all of the change
    for percent in all_change:
        # Appending the .text because I don't want a bunch of jibber
        all_percents.append(percent.text)
    # Return the second item because that is the one that I want
    return all_percents[2]


# Input is a ticker symbol and then will return price of ticker
def get_price(ticker):
    # Gets the website that we want to use and with market watch if you just add the ticker
    # symbol to this url then it will take you directly to its page basically
    response = requests.get('https://www.marketwatch.com/investing/stock/' + ticker)
    # Running soup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Scrapping to find where the price is because there is a lot of different
    # info on that website that can make it hard to scrape
    price = soup.find('body').find(class_='intraday__price').text
    # Returning the price and I do the [3:] with the string because it had a wierd $ symbol that I did not want
    # and did .rstrip() because it had a bunch of trailing character and new lines (\n) that I did now want and since
    # its the same on every page I can do it to every page that I am looking for the ticker on
    return price[3:].rstrip()


# Returns a list of all the changes ranging from 5 day to YTD
def all_change(ticker):
    # Getting the website
    response = requests.get('https://www.marketwatch.com/investing/stock/' + ticker)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Loops the all the classes that have the same name which are all the percent changes
    main_percent = soup.find_all(class_='content__item value ignore-color')
    # Making the main list that I am going to return
    all_percents = []
    # Looping through all of the percents and appending them to the main list that I am goint to return
    for percent in main_percent:
        # Doing the .text because it will just be a bunch of just random text you can't read
        all_percents.append(percent.text)
    # Pop the last element cause we don't need it
    all_percents.pop()
    # Returning the list of all the percentages
    return all_percents


# Takes in a list and then prints out the ticker symbol with the price and if the ticker symbol does not exist then it
# will print an error statement saying that the ticker does not exist
def sending_info(list):
    # Loops through all of the tickers in the list
    for ticker in list:
        # Try statement and if error then got to the except statement
        try:
            # Getting the price of ticker and setting it equal to variable callled "price"
            price = get_price(ticker)
            # Just the print statement using fprint which I now like a lot
            print(f"The current price of {ticker.upper()} is {price}")
        # If there is an AttributeError (which is when the ticker does not exist) go to this statement
        except AttributeError:
            # Simple print statment saying that the ticker does not exist
            print(f"{ticker.upper()} does not exist")
