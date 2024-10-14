# Module 6 Lab-6 
# Mat Bakarich
# October 10, 2024

# This module is for "The Cookout Calculator," it includes the hotdog and bun calculations and the instructions to print the results

# import python math module to be used later for formatting
import math
# import getdogs function
import getdogs


# declare variables
HOT_DOGS_PER_PKG = 10
BUNS_PER_PKG = 8 
dogs_left = 0
buns_left = 0
min_dogs = 0
min_buns = 0
total = getdogs.get_total_hot_dogs()


# define function to calculate numbers of packages required for hot dogs and buns
def show_results(total_hot_dogs):
    # calculate total leftover hot dogs
    dogs_left = (HOT_DOGS_PER_PKG - total % HOT_DOGS_PER_PKG) % HOT_DOGS_PER_PKG
    # calculate minimum packages of hot dogs required
    min_dogs = (total / HOT_DOGS_PER_PKG) + (0 ** (0 ** dogs_left))
    # format min_dogs to display whole numbers
    min_dogs = math.floor(min_dogs)
    # calculate total leftover buns
    buns_left = (BUNS_PER_PKG- (total % BUNS_PER_PKG)) % BUNS_PER_PKG
    # calculate minimum packages of hot dog buns required
    min_buns = (total/ BUNS_PER_PKG) + (0 ** (0 ** buns_left)) 
    # format min_buns to display whole numbers
    min_buns = math.floor(min_buns)

    
    # print the minimum number of packages of hot dogs and buns, and print the amount of leftover hot dogs and buns
    print(f'Minimum packages of hot dogs needed: {min_dogs}.' )
    print(f'Minimum packages of hot dog buns needed: {min_buns}.') 
    print(f'Hot dogs remaining:{dogs_left}.')
    print(f'Hot dog buns remaining:{buns_left}.') 
