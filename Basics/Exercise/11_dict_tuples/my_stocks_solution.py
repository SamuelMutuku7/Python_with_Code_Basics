portfolio = {"info": [600, 630, 620], "ril": [1430, 1490, 1567], "mtl": [234, 180, 160]}


def print_stock_prices():
    for stock, prices in portfolio.items():
        average = sum(prices) / len(prices)
        print(f"{stock} ==> {prices} ==> {average}")


def add_stock():
    stock_name = input("What is the name of the stock? ")
    user_price = input("What is its price?")
    user_price = int(user_price)
    if stock_name in portfolio:
        portfolio[stock_name].append(user_price)
    else:
        portfolio[stock_name] = [user_price]
    print_stock_prices()


def main():
    action = input("Enter operation (Print or Add): ")
    action = action.lower()
    if action == "print":
        print_stock_prices()
    else:
        add_stock()


if __name__ == "__main__":
    main()
