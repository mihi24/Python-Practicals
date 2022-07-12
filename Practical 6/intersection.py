# Find intesection between two Python lists using a list comprehension
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['b', 'd', 'e', 'f', 'g']
intersection = [item for item in list1 if item in list2]
print(intersection)