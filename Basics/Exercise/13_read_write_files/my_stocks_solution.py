with open("stocks.csv", "r") as stocks, open("my_stocks_output.csv", "w") as answer:
    answer.write("Company Name, PE Ratio, PB Ratio\n")
    next(stocks)
    for line in stocks:
        company, price, earnings, book_value = line.strip().split(",")
        price = float(price)
        earnings = float(earnings)
        book_value = float(book_value)
        pe_ratio = int(price / earnings)
        ptb_ratio = int(price / book_value)
        answer.write(f"{company}, {pe_ratio}, {ptb_ratio}\n")
# This code reads data from stocks.csv and writes the PE and PB ratios to my_stocks_output.csv.
# The code is almost identical to the original code, but it uses more descriptive variable names.
