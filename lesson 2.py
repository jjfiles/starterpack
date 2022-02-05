### Data Types ###

# integers or whole numbers
i = 0

# floats or floating point numbers (decimals)
f = 0.5

# string or text
s = "some text"

# Boolean or True / False
b = True

# if you ever want learn the type of a variable
# you can print(type(yourVariable))
print("DATA TYPES")
print(type(i))
print(type(f))
print(type(s))
print(type(b))


# In python indexing (or counting through something) starts at 0
# lists are a collection of variables or data
print('LISTS')
l = [0, 1, 2, 3]
print(l)

# you can mix and match data types
l = [0, i, f, s, b]
print(l)

# you can find the length or size of something in python with the len() function
print(len(l))

# if you want to access a specific item in a list you can do the following list[index]
print(l[3])

# to add something to a list that already contains data that you don't want to overwrite you can use the append function
l.append(1000)
print(l)
print(len(l))

# to remove something from a list you can list.remove(myVariable) or list.pop(index)
l.remove(1000)
print(l)
l.pop(0)
print(l)

# Tuples are collections of data that is ordered and you cannot change.
my_coords = (10, 12)

# to access data in a tuple works just the same way it does in a list
print("TUPLES")
print(my_coords)
print(my_coords[0])
print(my_coords[1])

# Sets are collections of data that are unordered and unchangable. Sets do not allow duplicate values
# Sets are also unindexed, meaning we can't access data the same way we can with the other collections
st = {"fruit", "vegtable", "water"}
print("SETS")
print(type(st))
print(st)

# Dictionaries are the last type of collection python offers
# Dictionaries are ordered. All dictionaries are key: value pairs
# keys must be unique but a value can repeat any number of times
print("DICTIONARIES")
d = {
    "brand": "Honda",
    "model": "Civic",
    "year": 2013,
    3: "Honda"
}

print(d)

# to access a value you give the dictionary the key dictionary[key]
print(d["brand"])


### OPERATORS ###
# very useful table -> https://www.w3schools.com/PYTHON/python_operators.asp
# basic operators
# = for assigning a value
q = 1

# to change the value of a variable you need to assign the changes back to itself
# + for addition - for subtraction
q = q + 10
q = q - 8

# for multiplication and division we use * and / respectfully
q = q * 2
q = q / 2

# for exponents we use **, to get the remainder of a division we use % (also known as modulous), and to get the quotient we use // (or truncated division)
q = q ** 2
print(q)
r = q % 2
print(r)
w = q // 2 
print(w)

# if you are using these to assign to an existing variable you can use and assignment operator to shorten it
# q = q + 1 becomes
q += 1

## Comparison ##
# to compare two things you use double equals ==, this gives you either True for False
print("BASIC COMPARISONS")
print(q == r)
print(q == 10)

# to check the opposite of a boolean value, you can use the ! symbol
print(q != 10)

# you also have access to greater than and less than with >, <, >=, <= for more basic comparisons

# Logic #
# the and operator gives True if both sides are True
print("LOGIC COMPARISONS")
print(q == 10 and q == 11)
print(q == 10 and q != 11)

# the or operator gives True if any of the comparisons are True
print(q == 10 or q == 11)

# the not operator gives us the opposite
print(not (q == 10 or q == 11))

# Identity #
print("IDENTITY COMPARISONS")

# you can use is or is not to check if something is equal, similar to = and !=
print(q is r)
print(q is not 11)

# MEMBERSHIP #
print("MEMBERSHIP COMPARISONS")
# in or not in can show you if a value is contained within some kind of collection
print("water" in st)
print("tree" in st)