#Importing all the stuff that I need for the webscrapping
import requests
from bs4 import BeautifulSoup

#Gets the list of all the tickers that you want to look up
def getting_list():
    #Making the main list that it will return
    the_list = []
    #Runs a while loop so people can enter in as many tickers as they want
    while True:
        #Asking for input
        response = input("Enter in the exact ticker symbol of the company (If no more than just hit enter): ")
        #If the input was not blank then append to list of tickers
        if response != "":
            the_list.append(response)
        #If it was blank then break out of while loop
        else:
            return the_list

#Input is a ticker symbol and then will return price of ticker
def get_price(ticker):
    #Gets the website that we want to use and with market watch if you just add the ticker
    #symbol to this url then it will take you directly to its page basically
    response = requests.get('https://www.marketwatch.com/investing/stock/' + ticker)
    #Running soup
    soup = BeautifulSoup(response.text, 'html.parser')
    #Scrapping to find where the price is because there is a lot of different
    #info on that website that can make it hard to scrape
    price = soup.find('body').find(class_ = 'intraday__price').text
    #Returning the price and I do the [3:] with the string because it had a wierd $ symbol that I did not want
    #and did .rstrip() because it had a bunch of trailing character and new lines (\n) that I did now want and since
    #its the same on every page I can do it to every page that I am looking for the ticker on
    return price[3:].rstrip()

#Takes in a list and then prints out the ticker symbol with the price and if the ticker symbol does not exist then it
#will print an error statement saying that the ticker does not exist
def sending_info(list):
    #Loops through all of the tickers in the list
    for ticker in list:
        #Try statement and if error then got to the except statement
        try:
            #Getting the price of ticker and setting it equal to variable callled "price"
            price = get_price(ticker)
            #Just the print statement using fprint which I now like a lot
            print(f"The current price of {ticker.upper()} is {price}")
        #If there is an AttributeError (which is when the ticker does not exist) go to this statement
        except AttributeError:
            #Simple print statment saying that the ticker does not exist
            print(f"{ticker.upper()} does not exist")

#Main function
def main():
    #Getting the list of tickers
    main_list = getting_list()
    #Sending all of those tickers to the print statment
    sending_info(main_list)
    #Just print done to indicate there are no more tickers to look up
    print("Done")

if __name__ == '__main__':
    main()