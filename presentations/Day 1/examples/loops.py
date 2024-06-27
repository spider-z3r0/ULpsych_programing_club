# This is a for loop

# Make a list of names
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Loop through the list and print each name
for name in names: #note the colon at the end of the line
    print(name) #note the indentation


# This is a for loop with an index
for i in range(len(names)): #note the colon at the end of the line
    print(f'{i}: {names[i]}') #note the indentation


# This is a loop in a loop
for name in names: #note the colon at the end of the line
    for letter in name: #note the colon at the end of the line
        print(letter) #note the indentation
    print('\n') #note the indentation