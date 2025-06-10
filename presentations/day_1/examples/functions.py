"""
   2. Make a list of 5 strings, make it 5 short strings, maybe the names of foods you like, or the names of your favourite movies.
   3. Use a `for loop` to print out each item in the list. 
       an example is in the `for_loops.py` file on brightspace.
   4. `def` a `function` that prints out each item in a list, and then `call` that function with the list you made in step 2.
       an example is in the `functions.py` file on brightspace.
   5. Look up the `methods` that allow to to make a string all uppercase, all lowercase, and to capitalize the first letter of each word.
   6. Modify your `function` so that it uses the `methods` you found in step 5 to `return` a new list with each item in the original list modified using the `string` method you passed to the function.
       - This should result in 3 new functions (there is a way to do this with only one function, but for now, make 3 separate functions that each use a different string method.)
       - An example of how to do this is in the `functions.py` file on brightspace.
"""

# Step 2
foods = ['apple', 'banana', 'carrot', 'dumpling', 'egg'] # list of 5 short strings

# Step 3
for food in foods: # for loop to print out each item in the list
    print(food)

# Step 4
def print_list(lst): # function that prints out each item in a list
    for item in lst:
        print(item)

print_list(foods) # call the function with the list from step 2

# Step 5
# methods to make a string all uppercase, all lowercase, and to capitalize the first letter of each word
# all uppercase = .upper()
# all lowercase = .lower()
# capitalize first letter of each word = .title()

# Step 6
def uppercase_list(lst): # function to return a new list with each item in the original list modified to all uppercase
    new_lst = []
    for item in lst:
        new_lst.append(item.upper())
    return new_lst

def lowercase_list(lst): # function to return a new list with each item in the original list modified to all lowercase
    new_lst = []
    for item in lst:
        new_lst.append(item.lower())
    return new_lst

def titlecase_list(lst): # function to return a new list with each item in the original list modified to capitalize the first letter of each word
    new_lst = []
    for item in lst:
        new_lst.append(item.title())
    return new_lst

upper_foods = uppercase_list(foods) # call the function with the list from step 2
lower_foods = lowercase_list(foods) # call the function with the list from step 2
title_foods = titlecase_list(foods) # call the function with the list from step 2

# sneaky combined loops and f strings
for i in range(len(foods)):
    print(f'{foods[i]} -> {upper_foods[i]} -> {lower_foods[i]} -> {title_foods[i]}') # print out the original list, the list modified to all uppercase, the list modified to all lowercase, and the list modified to capitalize the first letter of each word