class House():
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cashflow = 0
        self.roi = 0
        self.total_expenses = 0
        self.total_investment = 50000
        

    #3 Methods needed 
    #Income, Expenses, Cash flow, and ROI? for the final calculation

    def rental_income(self):
        self.income = float(input("How much income are you getting off this property a month?: "))
        print(f"Total income from your property is {self.income}")


    def rental_expenses(self):
        self.expenses_tax = float(input("How much is tax?: "))
        self.expenses_insurance = float(input("How much is insurance?: "))
        self.expenses_vancancy = float(input("How much for vancancy?: "))
        self.expenses_repairs = float(input("How much to put into repairs?: "))
        self.expenses_mortgage = float(input("How much is the monthly mortgage?: "))
        total_expenses = self.expenses_tax + self.expenses_insurance + self.expenses_vancancy + self.expenses_repairs + self.expenses_mortgage
        print(f"Total expenses comes out to {total_expenses}")

#Cash flow = income - expenses

    def cash_flow(self):
        self.cash_flow = self.income - self.total_expenses
        print(f"Your cash flow is {self.cash_flow}")

    def return_investment(self):
        total_investment = 50000
        self.roi = self.cash_flow / total_investment
        print(f"Your Return on Investment is {self.roi}")



x = House()
x.rental_income()
x.rental_expenses()
x.cash_flow()
x.return_investment()
#Math is not working after getting expenses for some reason?