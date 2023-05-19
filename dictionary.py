# Dictionaries in python

python_dictionary = {
    "Foo": "hello world",
    "Bar": "Baz"
}

# Accesing the dictionary
print(python_dictionary["Bar"])


# Adding a new item to dictionary
# This can be used to edit the dictionary as well
python_dictionary["Loop"] = "Hey there"

# Creating an empty dictionary
# This can be a method to empty it as well
empty_dictionary = {}

# Looping through a dictionary on python will give you only the keys
# The values have to be accessed manually
for key in python_dictionary:
    print(key)
    print(python_dictionary[key])

print(python_dictionary)
