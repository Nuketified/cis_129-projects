# cis129_lab03_coffeeShop.py
"""This script allows the user to adjust menu items and prices and output a receipt with the prices and tax."""
coffee = input( "How many coffees would you like?")# asks the user for an input for number of coffees.
muffin = input( "How many muffins would you like?")# asks the user for an input for number of muffins.
bagel = input( "How many bagels would you like?")# asks the user for an input for number of bagels.
cookie = input( "How many cookies would you like?")# asks the user for an input for number of cookies.
coffee = int(coffee) # defines the value coffee as an integer for arithmetic.
muffin = int(muffin) # defines the value muffin as an integer for arithmetic.
bagel = int(bagel) # defines the value bagel as an integer for arithmetic.
cookie = int(cookie) # defines the value cookie as an integer for arithmetic.
# currently only whole items are offered, if partial items are desired these can be set as floats instead.
pcoffee = float(5) # defines the value pcoffee as a float for arithmetic.
pmuffin = float(4) # defines the value pmuffin as a float for arithmetic.
pbagel = float (4.5) # defines the value pbagel as a float for arithmetic.
pcookie = float (2.5) # defines thevalue pcookie as a float for arithmetic.
# prices values set to floats because prices are rarely whole numbers
coffeet = coffee * pcoffee  # multiplies amount by price for a total price of coffee before tax.
muffint = muffin * pmuffin # multiplies amount by price for a total price of muffins before tax.
bagelt = bagel * pbagel # multiplies amount by price for a total price of bagels before tax.
cookiet = cookie * pcookie # multiplies amount by price for a total price of cookies before tax.
tax = (coffeet + muffint + bagelt + cookiet) * .06 # finds the tax amount on the subtotal.
coffeetf =  format(coffeet, ".2f") # formats coffeet to display 2 decimal points including .00 for prices.   
muffintf =  format(muffint, ".2f") # formats muffint to display 2 decimal points including .00 for prices.
bageltf = format(bagelt, ".2f") # formats bagelt to display 2 decimal points including .00 for prices.
cookietf = format(cookiet, ".2f") # formats cookiet to display 2 decimal points including .00 for prices.
taxf = format(tax, ".2f") # formats tax to display 2 decimal points including .00 for prices.
total = format((coffeet + muffint + bagelt + cookiet + tax), ".2f") # defintes total as the sum of coffeet, muffint, bagelt, cookiet and tax, then formats tax to display 2 decimal points including .00 for prices.
print (f"***************************************\nMy Coffee and Muffin Shop\nNumber of coffees bought?\n{coffee}\nNumber of muffins bought?\n{muffin}\nNumber of bagels bought?\n{bagel}\nNumber of cookies bought?\n{cookie}\n***************************************\n\n***************************************\nMy Coffee, Muffin, Bagel, and Cookie Shop Receipt\n\n{coffee} Coffee at $5 each: $ {coffeetf}\n{muffin} Muffins at $4 each: $ {muffintf}\n{bagel} Bagel at $4.50 each: $ {bageltf}\n{cookie} Cookie at $4.50 each: $ {cookietf}\n6% tax: $ {taxf}\n---------\nTotal $ {total}\n***************************************") # prints a receipt showing number of coffees, muffins, bagels, and cookies purchased, subtotals for each, tax, and a total. 
# Thanks for using this program! For any issues I can be reached at mbakarich1@mail.pima.edu, thanks and enjoy :)
