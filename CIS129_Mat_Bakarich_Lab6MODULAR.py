# Module 6 Lab-6 
# Mat Bakarich
# October 10, 2024


# The Cookout Calculator #


# This program takes user input for the number of cookout attendees and how many hot dogs each person would like, then calculate the minimum numbers of packages of buns and hot dogs required.


# import function to calculate total hot dogs required for the cookout
import getdogs
# import function to calculate numbers of packages required for hot dogs and buns
import showdogs

# Declare variables
total_hot_dogs = 0
attendees = 0
hot_dogs = 0

# call function get_total_hot_dogs
getdogs.get_total_hot_dogs()
# call function show_results
showdogs.show_results(total_hot_dogs)

