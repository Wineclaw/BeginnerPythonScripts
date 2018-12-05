# Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# Write a loop that prints each of the numbers on a new line.
# Write a loop that prints each number and its square on a new line.
# Write a loop that adds all the numbers from the list into a variable called total. You should set the total variable to have the value 0 before you start adding them up, and print the value in total after the loop has completed.
# Print the product of all the numbers in the list. (product means all multiplied together)
#

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# assigns list to xs


for given_list in xs:
    print(given_list)          # prints number on a new line
    print(given_list ** 2)     # prints square of previous number on a new line

total = 0 # sets total to 0

for given_list in xs:
    total = given_list + total
    
print("The total is", total)
# totals all numbers

total = 1
# resets total to 1, else 0 will never increase from 0

for given_list in xs:
    total = given_list * total
    
print("The product of the list is", total)
# product of all numbers in list