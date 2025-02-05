import datetime

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
        self.transaction_history = []

    def add_stock(self, ticker, shares, purchase_price, purchase_date=None):
        if purchase_date is None:
            purchase_date = datetime.date.today()
        else:
            purchase_date = datetime.datetime.strptime(purchase_date, "%Y-%m-%d").date()

        if ticker in self.portfolio:
            self.portfolio[ticker]['shares'] += shares
        else:
            self.portfolio[ticker] = {'shares': shares, 'purchase_price': purchase_price, 'purchase_date': purchase_date}

        self.transaction_history.append({'action': 'Add', 'ticker': ticker, 'shares': shares, 'price': purchase_price, 'date': purchase_date})

    def remove_stock(self, ticker, shares_to_remove=None):
        if ticker in self.portfolio:
            current_shares = self.portfolio[ticker]['shares']
            if shares_to_remove is None or shares_to_remove >= current_shares:
                removed_shares = current_shares
                del self.portfolio[ticker]
            else:
                removed_shares = shares_to_remove
                self.portfolio[ticker]['shares'] -= shares_to_remove

            self.transaction_history.append({'action': 'Remove', 'ticker': ticker, 'shares': removed_shares, 'price': None, 'date': datetime.date.today()})
        else:
            print(f"Ticker {ticker} not found in portfolio.")

    def get_portfolio_value(self):  # Calculates based on purchase price
        total_value = 0
        for ticker, data in self.portfolio.items():
            total_value += data['purchase_price'] * data['shares']
        return total_value

    def get_profit_loss(self):  # Profit/loss is meaningless without current price
        print("Profit/Loss cannot be calculated without current stock prices.")
        return None

    def analyze_diversification(self):
        total_investment = sum(data['shares'] * data['purchase_price'] for data in self.portfolio.values())
        print("Diversification Analysis:")
        for ticker, data in self.portfolio.items():
            investment = data['shares'] * data['purchase_price']
            percentage = (investment / total_investment) * 100 if total_investment > 0 else 0
            print(f"{ticker}: Investment: ${investment:.2f}, Percentage: {percentage:.2f}%")

    def calculate_tax_implications(self, tax_rate):
        print("Tax implications cannot be calculated without knowing gains/losses.")
        return None

    def display_portfolio(self):
        print("Current Portfolio:")
        for ticker, data in self.portfolio.items():
            print(f"{ticker}: Shares: {data['shares']}, Purchase Price: ${data['purchase_price']:.2f}, Purchase Date: {data['purchase_date']}")

    def display_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)


def portfolio_tracker():
    portfolio = StockPortfolio()

    while True:
        print("\nMenu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Display Transaction History")
        print("5. Get Portfolio Value")
        print("6. Get Profit/Loss")
        print("7. Analyze Diversification")
        print("8. Calculate Tax Implications")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == '1':  # Add Stock
            ticker = input("Enter stock ticker: ")
            shares = int(input("Enter number of shares: "))
            purchase_price = float(input("Enter purchase price: "))
            purchase_date = input("Enter purchase date (YYYY-MM-DD) or leave blank for today: ")
            portfolio.add_stock(ticker, shares, purchase_price, purchase_date if purchase_date else None)

        elif choice == '2':  # Remove Stock
            ticker = input("Enter stock ticker to remove: ")
            shares_to_remove = input("Enter number of shares to remove (or leave blank to remove all): ")
            shares_to_remove = int(shares_to_remove) if shares_to_remove else None
            portfolio.remove_stock(ticker, shares_to_remove)

        elif choice == '3':  # Display Portfolio
            portfolio.display_portfolio()

        elif choice == '4':  # Display Transaction History
            portfolio.display_transaction_history()

        elif choice == '5':  # Get Portfolio Value value = portfolio.get_portfolio_value()
            if value is not None:
                print(f"Total Portfolio Value (based on purchase price): ${value:.2f}")

        elif choice == '6':  # Get Profit/Loss
            profit_loss = portfolio.get_profit_loss()

        elif choice == '7':  # Analyze Diversification
            portfolio.analyze_diversification()

        elif choice == '8':  # Calculate Tax Implications
            tax_rate = float(input("Enter tax rate (as a decimal): "))
            tax = portfolio.calculate_tax_implications(tax_rate)

        elif choice == '9':  # Exit
            print("Exiting the portfolio tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    portfolio_tracker() 
