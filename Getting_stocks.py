# All of the imports
from Web_scraping import *
import openpyxl

# Showing where my excel file is
excel_file = '/Users/kazu.umemoto/Desktop/Learning_Python/Web-Scraping/Stocks.xlsx'
# Loading up the excel file
workbook = openpyxl.load_workbook(excel_file)
# Loading up "Sheet1" and setting it as the one that I want to work on
worksheet = workbook['Sheet1']


def main():
    # Dictionary to keep track of what row certain tickers are on
    diction = {}
    # Counter that will go up as up as we go row to row and starts at 2 because first row just has the labels
    counter = 2
    # While loop that will run until the row has no value in it so that I don't have to use a for loop and
    # keep updating it when I want to add another ticker
    while worksheet['A' + str(counter)].value != None:
        # Makes a new key with the counter and then gets the ticker symbol and sets it equal to the key
        diction[counter] = worksheet['A' + str(counter)].value
        # Counter goes up 1 so that it goes to the next row
        counter += 1
    # For loop that will loop through all of the keys in the dictionary
    for keys in diction:
        # Gets the price of the ticker
        price = get_price(diction[keys])
        # Gets the percentage change for the ticker while the market was open
        percentages = all_change(diction[keys])
        # Gets a list of all the other changes like 5 day, 1 month, 3 month, and YTD change
        day = day_change(diction[keys])
        # Puts the value of the ticker in the sheet
        worksheet['B' + str(keys)] = price
        # Puts the change of stock during the day in the sheets. I only use [:-1] so that I don't get the
        # percentage symbol included and divides by 100 because excel does somethings funky so I have to divide it
        # so that it goes in correctly
        worksheet['E' + str(keys)] = float(day[:-1]) / 100
        # Puts the value of the 5 day change in the sheet
        worksheet['F' + str(keys)] = float(percentages[0][:-1]) / 100
        # Puts the value of the 1 month change in the sheet
        worksheet['G' + str(keys)] = float(percentages[1][:-1]) / 100
        # Puts the value of the 3 month change in the sheet
        worksheet['H' + str(keys)] = float(percentages[2][:-1]) / 100
        # Puts the value of the YTD change in the sheet
        worksheet['I' + str(keys)] = float(percentages[3][:-1]) / 100
    # Saves the file
    workbook.save(excel_file)


# Runs the main function
if __name__ == '__main__':
    main()
