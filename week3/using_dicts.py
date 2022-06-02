state_capitals = {"Washington" : "Olympia", "Oregon" : "Salem", "California" : "Sacramento"}
#print(len(state_capitals))

# You can find the value for any key by simply printing it with the key in []
#print(state_capitals["Washington"])

#Dictionaries are Mutable - Adding, Modifying, or Removing Key Value Pairs
''''''
#Modifying
state_capitals["Washington"] = "Aberdeen"
print(state_capitals)

#Adding
state_capitals["Texas"] = "Austin"
print(state_capitals)

#Removing
#     del method ---Gone forever
del state_capitals["California"]
print(state_capitals)
#     pop method ---Can be assigned to a variable if needed such as removed_capital = state_capitals.pop("Oregon") ----would return "Oregon"
state_capitals.pop("Oregon")
