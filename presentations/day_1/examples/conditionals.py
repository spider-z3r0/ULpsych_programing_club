# This file contains examples of conditional statements in Python.

# Make a dictionary of 5 key-value pairs with mixed types.

d1 = {'name': 'Alice', 'age': 25, 'fav_foods': ['apple', 'banana', 'carrot'], 'fav_food_score': {'apple': 10, 'banana': 3, 'carrot': 7}, 'is_vegetarian': True}

if d1['is_vegetarian'] == True:
    print(f"{d1['name']} is a vegetarian.")
else:
    print(f"{d1['name']} is not a vegetarian.")

if d1['age'] >= 21:
    print(f"{d1['name']} is old enough to drink.")
elif d1['age'] >= 18:
    print(f"{d1['name']} is old enough to vote.")
else:
    print(f"{d1['name']} is not old enough to vote or drink.")

if d1['fav_foods']['apple'] > 7:
    print(f"{d1['name']} really likes apples.")
elif d1['fav_foods']['apple'] > 3:
    print(f"{d1['name']} likes apples.")
else:
    print(f"{d1['name']} does not like apples.")
