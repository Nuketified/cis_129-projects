# Module 7 Lab 7
# Mat Bakarich
# Oct 18, 2024

#################################################
# Theatre Seating Calculato r#
#################################################

# this program displays seating prices per section, then gets user input for seat sales, then outputs the totals for sales data




# define constants
#################################################
# add new seat sections by adding constants below:
#################################################
# number of seats in each section
SECTION_SEATS = (300, 500, 200, 100)
# ticket prices for sections
TICKET_PRICE = (20, 15, 10, 7.5)
# section names
SECTION = ("A", "B", "C", "D") 
# number of sections
NUMBER_OF_SECTIONS = 4
#################################################
#################################################



# multiply the ticket price by the number of tickets sold in a section and returns that value
def total_sales(tickets_sold):    
    total_sales = float(TICKET_PRICE[counter_b] * tickets_sold) 
    return total_sales 

# display text to user to get user input, take the user inputs and print the totals to the user.
def main():
    # define variables
    #################################################
    # add "0"s below in "subtotal" and "tickets_total" to add sections
    #################################################
    subtotal = [0, 0, 0, 0]
    tickets_total = [0, 0, 0, 0]    
    #################################################
    #################################################
    counter_a = 0
    global counter_b 
    counter_b = 0
    counter_c = 0
    
    # print a Welcome message and display section names, seat prices, number of seats per section
    print("Welcome!")
    while counter_a < NUMBER_OF_SECTIONS:
        print("There are ", SECTION_SEATS[counter_a], " seats in section ", SECTION[counter_a]," at $",TICKET_PRICE[counter_a],".",sep="" )
        counter_a+=1
    
    # get user input for seats sold in each section
    while counter_b < NUMBER_OF_SECTIONS:
        # validate inputs 
        while True:
            try:
                # get user input for seats sold in section 
                tickets_sold = int(input(f"How many seats sold in section {SECTION[counter_b]}?"))
            except ValueError:
                print(f"Input must be a postive integer less than or equal to {SECTION_SEATS[counter_b]}")  
                continue
            if tickets_sold > SECTION_SEATS[counter_b]:
                print(f"Input must be a postive integer less than or equal to {SECTION_SEATS[counter_b]}")
                continue
            if tickets_sold < 1:
                print(f"Input must be a positive integer less than or equal to {SECTION_SEATS[counter_b]}")
                continue
            else:
                break
    

       


        # print the subtotal for the current section
        print(f"The total for ticket sales in Section {SECTION[counter_b]} is: ${total_sales(tickets_sold):,.2f}.")
        # store values to print later
        # call function to get total sales
        subtotal[counter_b]= total_sales(tickets_sold)
        # subtotal[counter_b]= (f"{subtotal[counter_b]:.2f}")
        tickets_total[counter_b] = tickets_sold
        counter_b+=1

    # print totals for each section
    print("\nThe totals for each section are:\n")
    while counter_c < NUMBER_OF_SECTIONS:
        print(SECTION[counter_c],": ",tickets_total[counter_c]," seats at $",TICKET_PRICE[counter_c], " = $",subtotal[counter_c],".",sep="") 
        counter_c+=1
    
    # print the grand total             
    print(f"\nThe grand total is: $", sum(subtotal),".", sep="")

# call main function
main()
