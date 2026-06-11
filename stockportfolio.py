
# stock portfolio tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300
}

total_value = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock_name = input("\nEnter stock name(or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quality: "))    

        investment = stocks[stock_name] * quantity
        total_value += investment

        print(f"{stock_name} Investment Value: ${investment}")

    else:
        print("stock doesn't found")    

print("===== PORTFOLIO SUMMARY =====")        
print(f"Total Investment value: ${total_value}")

with open("portfolio_summary.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write(f"Total Investment value: ${total_value}")

print("Portfolio summary saved to portfolio_summary.txt")    