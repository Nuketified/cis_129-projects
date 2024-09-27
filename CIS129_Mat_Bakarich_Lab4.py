# Module 5 Lab-5 
# Mat Bakarich 
# September 29, 2024
# This program calculates and prints the results of the company's new bonus structure after asking a user to input the monthly sales and sales increase percentage as a decimal.

# The main function 
def main():
    # declare local variables 
    monthlySales = getSales("Please enter the monthly sales in dollars.  ") # monthly sales amount
    storeAmount = calcStoreBonus(monthlySales) # store bonus amount
    salesIncrease = getIncrease("Please enter the sales increase as a percent.  ") # percent of sales increase
    EmpAmount = calcEmpBonus(salesIncrease) # employee bonus amount
    printBonus(storeAmount, EmpAmount)
    # call to getSales(sales = getSales())
    # call to getIncrease(increase = getIncrease())
    # call to calcStoreBonus(StoreBonus = calcStoreBonus())
    # call to calcEmpBonus(EmpBonus = calcEmpBonus())
    # call to printBonus(printStoreBonus() = printBonus, printEmpBonus() = printBonus

    # This function gets the monthly sales.
def getSales(prompt):
        monthlySales = float(input(prompt))
        return monthlySales

    # This function gets the percent of increase in sales.
def getIncrease(prompt):
        salesIncrease = float(input(prompt))
        salesIncrease = salesIncrease/100
        return salesIncrease

    # This function determines the storeAmount bonus.
def calcStoreBonus(monthlySales):
        if monthlySales >= 110000:
            storeAmount = 6000
        elif monthlySales >= 10000:
            storeAmount = 5000
        elif monthlySales >= 9000:
            storeAmount = 4000
        elif monthlySales >= 8000:
            storeAmount = 3000
        else:storeAmount = 0
        return storeAmount

        # This function determines the empAmount bonus.
def calcEmpBonus(salesIncrease):
            if salesIncrease >= .05:
                empAmount = 75
            elif salesIncrease >= .04:
                empAmount = 50
            elif salesIncrease >= .03:
                empAmount = 40
            else:
                empAmount = 0
            return empAmount

        # This function prints the bonus information.
def printBonus (storeAmount, empAmount):
            print("The store bonus amount is $", storeAmount)
            print("The employee bonus amount is $", empAmount)
            if (storeAmount == 6000) and (empAmount == 75):
                print('Congrats you have reached the highest bonus amounts possible!')
        # calls main
main()
