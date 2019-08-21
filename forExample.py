#This is how we do comments, we use octothorpes

#The following link has a list of functions for strings in python:
#https://www.w3schools.com/python/python_ref_string.asp


fishySentence = "fish fish fish"

#list
inTheNet = ["bass", "salmon", "blowfish"]

#tuple --like a list but it is immutable
encasedInIce = ("pike", "serpent")

#sets --unordered, items can not be removed/changed, but may be added
fishySet = {"FregeFish, GodelFish, HofstadterFish"}

#dictionary --sort of like an object with properties in key/value pairs
dictionaryFish = {
    "cover" : "A picture of a fish entitled dictionary",
    "introduction" : "The text reads 'in a world...' " ,
}

#I'm going to demonstrate the usage of the count() method
print("The number of fish in the fishy sentence is: " )
print(fishySentence.count("fish"))


#Here is how we iterate over an array of strings and print the output to console
print("\nHere are the all the fish inTheNet")
for fish in inTheNet:
    print(fish)


print("\nCapitalized")
for fish in inTheNet:
    print(fish.capitalize())

#I'm going to demonstrate the usage of the different collections tomorrow!