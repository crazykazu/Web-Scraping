from Web_scraping import *
import openpyxl
from string import ascii_uppercase

excel_file = '/Users/kazu.umemoto/Desktop/Learning_Python/Web-Scraping/Stocks.xlsx'

workbook = openpyxl.load_workbook(excel_file)
worksheet = workbook['Sheet1']

def main():
    diction = {}
    counter = 2
    while worksheet['A' + str(counter)].value != None:
        diction[counter] = worksheet['A' + str(counter)].value
        counter += 1
    for keys in diction:
        price = get_price(diction[keys])
        worksheet['B' + str(keys)] = price
    workbook.save(excel_file)

main()
