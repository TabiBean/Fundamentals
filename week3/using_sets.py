#numbers_set = {1, 2, 3, 4, 4} #duplicate values get removed
#The second 4 does not appear

#numbers_set = {1, 2, 3, 4, [5, 6]} causes an error: TypeError: unhashable type: 'list'

numbers_set = (1, 2, 3,4, (5, 6)) #a tuple can be used because it is immutable

print(numbers_set)

words_set = {"Alpha", "Bravo", "Charlie"} #strings can be used because they are immutable

#for...in loop
abcd = ""
for word in words_set:
    abcd += word
print(abcd)

#sets are searchable
if "Alpha" in words_set:
    print("Alpha is in set.")
else:
    print("Alpha is not in set. ")

#Adding to a set
words_set.add("Delta")
print(words_set)

#Removing from a set
words_set.discard("Bravo")
print(words_set)

colors = {"000000": "black", "ffffff": "white", "dc143c": "crimson"}
print(colors["dc143c"])


