
#************Dictionaries*********

# Dictionaries are special structures in python which allows us to store information which are called key value pair. Dictionaries contains a key and a value. Each key refer to its definition and every key in the dictionary has to be unique. The keys can be strings, numbers  etc.....
# Whenever we want to make dictionaries, it should be written inside the {........}

monthConversions={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "My":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
    
}

# There are different ways of getting the definition using the key value
#1)
print(monthConversions["Jan"])

#2)
print(monthConversions.get("Feb"))

#3)
print(monthConversions.get("abc","Not a valid key"))

