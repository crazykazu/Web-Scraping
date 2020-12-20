# The imports for the GUI and web-scraping stuff to get like prices and percentages
from Web_scraping import *
import tkinter as tk


# The main function that will make labels, append them to a list, and then pack them onto the root
def getStock():
    # Try statment just in case the ticker does not exist
    try:
        # The main list that will have all of the Labels
        main_list = []
        # Gets the price
        price = get_price(ticker.get())
        # Gets the change in price over the day
        change_in_day = day_change(ticker.get())
        # Gets all of the other changes like 5 day, 3 month, etc.
        every_change = all_change(ticker.get())
        # Appends all of these labels to the list
        main_list.append(tk.Label(root, text="Ticker: " + ticker.get().upper()))
        main_list.append(tk.Label(root, text="Price: " + str(price)))
        main_list.append(tk.Label(root, text="Change today: " + str(change_in_day)))
        main_list.append(tk.Label(root, text="Change in 5 days: " + str(every_change[0])))
        main_list.append(tk.Label(root, text="Change in 1 month: " + str(every_change[1])))
        main_list.append(tk.Label(root, text="Change in 3 month: " + str(every_change[2])))
        main_list.append(tk.Label(root, text="Change from YTD: " + str(every_change[3])))
        # Loops through the whole list and packs all of the labels instead of like going
        # one by one doing it
        for text in main_list:
            text.pack()
    # If the ticker does not exist then we get an AttributeError and will print an error statement
    except AttributeError:
        error_label = tk.Label(root, text="The ticker " + ticker.get().upper() + " does not exist")
        error_label.pack()


# Making the root
root = tk.Tk()

# Making the button that will run the getStock function
findStock = tk.Button(root, text='Enter Stock Ticker', fg='black', command=getStock)
findStock.pack()

# Text box to enter in the ticker
ticker = tk.Entry(root, width=5, bg='black', fg='white', borderwidth=3)
ticker.pack()

# Just running the main loop
root.mainloop()
