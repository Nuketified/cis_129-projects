coffee = input( "How many coffees would you like?")
muffin = input( "How many muffins would you like?")
coffee = int(coffee)
muffin = int(muffin)
pcoffee = float(5)
pmuffin = float(4)
coffeet = coffee * pcoffee
muffint = muffin * pmuffin
coffeet = float(coffeet)
muffint = float(muffint)
tax = (coffeet + muffint) * .06
tax = float(tax)
coffeetf =  format(coffeet, ".2f") 
muffintf =  format(muffint, ".2f")
taxf = format(tax, ".2f")
total = coffeet + muffint + tax
print (f"***************************************\nMy Coffee and Muffin Shop\nNumber of coffees bought?\n{coffee}\nNumber of muffins bought?\n{muffin}\n***************************************\n\n***************************************\nMy Coffee and Muffin Shop Receipt\n{coffee} Coffee at $5 each: $ {coffeetf}\n{muffin} Muffins at $4 each: $ {muffintf}\n6% tax: $ {taxf}\n---------\nTotal $ {total}\n***************************************")
