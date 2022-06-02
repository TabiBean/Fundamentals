
states = ["Washington", "Oregon", "California"]
print(states[0])
print(states[1])
print(states[2])

#To access the last item on the list [-1]
print(states[-1])
print(states[-2])
print(states[-3])


states = ["Washington", "Oregon", "California"]

states[2] = "Arizona"
#Prints the entire list: print(states)

#How many items are in a list
#print(len(states))

#METHODS
# listname.methodname(arguments)

# append will add an item to the end of a list
states.append("New York")
#print(states)

# pop will pop the last item off the end of a list
states.pop()
#print(states)

# pop with an argument will pop off that item number
states.pop(1)
print(states)











