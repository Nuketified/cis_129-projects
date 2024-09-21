# cis129_lab03_coffeeShop.py
"""This script allows the user to input numbers of items a customer wants and output a receipt with the prices and tax."""
coffee = input( "How many coffees would you like?") # asks the user for an input for number of coffees.
muffin = input( "How many muffins would you like?") # asks the user for an imput for number of muffins.
coffee = int(coffee) # sets the value for coffee to an integer.
muffin = int(muffin) # sets the value of muffin to an integer.
pcoffee = float(5) # sets the price of coffee as a float.
pmuffin = float(4) # sets the price of coffee as a float.
coffeet = coffee * pcoffee # multiplies amount by price for a total price of coffee before tax.
muffint = muffin * pmuffin # multiplies amount by price for a total price of muffins before tax.
coffeet = float(coffeet) # sets cofeet to a float, possibly redundant
muffint = float(muffint) # sets muffint to a float, possibly redundant
tax = (coffeet + muffint) * .06 # finds the tax amount on the subtotal.
tax = float(tax) #sets the tax to a float, possibly redundant.
coffeetf =  format(coffeet, ".2f") # formats coffeet to display 2 decimal points including .00 for prices.
muffintf =  format(muffint, ".2f") # formats muffint to display 2 decimal points including .00 for prices.
taxf = format(tax, ".2f") # formats tax to display 2 decimal points including .00 for prices.
total = coffeet + muffint + tax # defintes total as the sum of coffeet, muffint, and tax.
print (f"***************************************\nMy Coffee and Muffin Shop\nNumber of coffees bought?\n{coffee}\nNumber of muffins bought?\n{muffin}\n***************************************\n\n***************************************\nMy Coffee and Muffin Shop Receipt\n{coffee} Coffee at $5 each: $ {coffeetf}\n{muffin} Muffins at $4 each: $ {muffintf}\n6% tax: $ {taxf}\n---------\nTotal $ {total}\n***************************************") # prints a receipt showing number of coffees and muffins purchased, subtotals for each, tax, and a total. This should be cleaned up using triple quotes
