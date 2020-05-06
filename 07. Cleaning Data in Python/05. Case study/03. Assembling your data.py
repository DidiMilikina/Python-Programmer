'''
Assembling your data
Here, three DataFrames have been pre-loaded: g1800s, g1900s, and g2000s. These contain the Gapminder life expectancy data for, respectively, the 19th century, the 20th century, and the 21st century.

Your task in this exercise is to concatenate them into a single DataFrame called gapminder. This is a column-wise concatenation, similar to how you concatenated the Ebola dataset with information about patients in Chapter 3.

Instructions
100 XP
Use pd.concat() to concatenate g1800s, g1900s, and g2000s along the column axis into one DataFrame called gapminder. Make sure you pass DataFrames to pd.concat() in the form of a list.
Print the shape and the head of the concatenated DataFrame.
'''
# Concatenate the DataFrames column-wise
gapminder = pd.concat([g1800s, g1900s, g2000s], axis = 1)

# Print the shape of gapminder
print(gapminder.shape)

# Print the head of gapminder
print(gapminder.head())
