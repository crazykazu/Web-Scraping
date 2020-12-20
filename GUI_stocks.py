from Web_scraping import *
import tkinter as tk

'''
def clear():
    root.option_clear()
'''
def getStock():
    try:
        main_list = []
        price = get_price(ticker.get())
        change_in_day = day_change(ticker.get())
        every_change = all_change(ticker.get())
        main_list.append(tk.Label(root, text="Price: " + str(price)))
        main_list.append(tk.Label(root, text="Change today: " + str(change_in_day)))
        main_list.append(tk.Label(root, text="Change in 5 days: " + str(every_change[0])))
        main_list.append(tk.Label(root, text="Change in 1 month: " + str(every_change[1])))
        main_list.append(tk.Label(root, text="Change in 3 month: " + str(every_change[2])))
        main_list.append(tk.Label(root, text="Change from YTD: " + str(every_change[3])))
        for text in main_list:
            text.pack()
    except AttributeError:
        error_label = tk.Label(root, text="The ticker " + ticker.get() + " does not exist")
        error_label.pack()


root = tk.Tk()

findStock = tk.Button(root, text='Enter Stock Ticker', fg='black', command=getStock)
findStock.pack()

want_clear = tk.Button(root, text='Clear Board', fg='black', command=clear)
want_clear.pack()

ticker = tk.Entry(root, width=5, bg='black', fg='white', borderwidth=3)
ticker.pack()

root.mainloop()
