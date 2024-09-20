coffee = input( "How many coffees would you like?")
muffin = input( "How many muffins would you like?")
coffee = int(coffee)
muffin = int(muffin)
coffeet = coffee * 5
coffeet = int(coffeet)
muffint = muffin * 4
muffint = int(muffint)
tax = (coffeet + muffint) * 1.06
tax = int(tax)
total = coffeet + muffint +tax
print ("***************************************\nMy Coffee and Muffin Shop\nNumber of coffees Bought?\ncoffee\nNumber of muffins bought?\nmuffin\n***************************************\n\n***************************************\nMy Coffee and Muffin Shop Receipt\ncoffee Coffee at $5 each: $ coffeet.00\nmuffin Muffins at $4 each: $ muffint.00\n6%tax: $ tax\n---------\nTotal $ total\n***************************************")
