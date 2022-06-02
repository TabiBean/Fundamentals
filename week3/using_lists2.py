
states = ["Washington", "Oregon", "California"]

'''
# How ar for loop runs through a list
for state in states:
    state = state.lower()
    print(state)

#Another way to loop through lists to check if an item appears in the list
print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)
'''
'''
#Adding two lists together
states2 = ["Arizona", "Ohio", "Texas", "Louisiana"]
best_states = states + states2
print(best_states)

#Slicing Notation for lists

#[1:3] grabs up to but not including items 1 and 2 and does not grab item 3
print(best_states[1:3])

#[ : 5] grabs all the items from the start up to item 4
print(best_states[ :4])

# [4: ] grabs all the items from item 4 to the end of the list
print(best_states[4:])
'''

#Using Negative numbers in slicing notation

my_list = ["apples", "oranges", "berries", "grapes"]
print(my_list[-1]) 
#This prints grapes showing the negative notation sliced off the last item on the list

print(my_list[-4: -3])
#This prints ['apples'], showing the negative picked out the 4th item from the bottom of the list.

print(my_list[-1: ])
#This prints ['grapes'], showing the negative removed the last item

print(my_list[-4: ])
#This prints ['apples', 'oranges', 'berries', 'grapes'], showing the last 4 items removed

'''Conclusion slicing works in reverse when using negative numbers but still functions the same way as positive numbers except positive numbers go from beginning to end while negative numbers go from the end to the beginning.'''





















