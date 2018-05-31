from selenium import webdriver

driver = webdriver.Safari()
expedia = 'https://www.expedia.co.uk/Flights-Search?flight-type=on&starDate=24%2F07%2F2018&_xpid=11905%7C1&mode=search&trip=oneway&leg1=from%3ALondon%2C+England%2C+UK+%28LON-All+Airports%29%2Cto%3ABucharest%2C+Romania%2Cdeparture%3A24%2F09%2F2018TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY'
driver.get(expedia)
flight_prices = driver.find_elements_by_class_name("full-bold no-wrap") 

"""maximum price = input() + try again"""

max_price = int(input("Maximum price in pounds? Enter digits only: "))
prices = []
symbol = []
for price in flight_prices:
    price = price.text
    price = price.replace(price[0], "")
    price = int(price.replace(',', ''))
    symbol.append(price)

symbol = sorted(set(symbol))

for price in symbol:
    if price < max_price: 
        price = str(price)
        price = '£'+price
        prices.append(price)

prices = str(prices)[1:-1] #converts the set into a string
prices = prices.replace("'", "")


if prices != "":
    print("Under £{1}, available tickets found are at {0}. Please check www.expedia.co.uk for more details.".format(prices, max_price))
else:
    print("No tickets found below the mentiond price.")  
    try_again = input("Do you want to try again? Yes/No.")
    while True:
        if try_again.lower() == "yes":
            max_price = int(input("Maximum price in pounds? Enter digits only: "))
            prices = []
            symbol = []
            for price in flight_prices:
                price = price.text
                price = price.replace(price[0], "")
                price = int(price.replace(',', ''))
                symbol.append(price)

            symbol = sorted(set(symbol))
    
            for price in symbol:
                if price < max_price: 
                    price = str(price)
                    price = '£'+price
                    prices.append(price)

            prices = str(prices)[1:-1] #converts the set into a string
            prices = prices.replace("'", "")
            print("Under £{1}, available tickets found are at {0}. Please check www.expedia.co.uk for more details.".format(prices, max_price))
            break
        elif try_again.lower() == "no":
            print("Thank you. Goodbye!")
            break
        else:
            print("Input has to be 'yes' or 'no'.")
            try_again = input("Do you want to try again? Yes/No.")     
