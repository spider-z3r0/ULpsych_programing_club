import pandas as pd #importaing pandas with the nickname pd
# initialise some list objects that contains our data, this could also be a list of lists, or a dict of lists for example
names = ['John Lennon', 'Morris Day', 'Robert Rtujillo', 'Prince', 'Pete Best', 'Frank Zappa']
bands = ['Beatles', 'The Time', 'metalica', 'The Time', 'Beatles', 'The Mothers']
instruments = ['Guitar', 'Vocals', 'Bass', 'Multi', 'Drums', 'Multi']
writer = ['yes', 'no', 'no', 'yes', 'no', 'yes']
orig = ['yes', 'yes', 'no', 'yes', 'yes', 'yes']
bands_df = pd.DataFrame(# opening brackets but moving to new line for readability, note the uppercase D and F in the call
    list(zip(names,bands, instruments, writer, orig )), #first argument note the comma at the end of it, this is a couple of nested functions
    columns = ['Participant name', 'band', 'instrument', 'song writer', 'original member']# second argument , passing a list to the columns arguments
    )# closing the first pair of brackets to complete the function call