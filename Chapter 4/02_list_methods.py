friends = ["Apple", "Orange", 5, 345.04, "Naman", "Rohan"]
print(friends)
friends.append("Harry")
print(friends)

l1 = [1, 6, 4, 10, 23, 15]
# l1.sort() 
# l1.reverse() 
# l1.insert(3, 245)  Insert 245 such that its index in the list is 3
# value = (l1.pop(3))
# print(value)   
l1.remove(23)
print(l1)



numbers = [5, 2, 9, 1]
numbers.sort()  # Ascending
print(numbers)  # Output: [1, 2, 5, 9]

numbers.sort(reverse=True)  # Descending
print(numbers)  # Output: [9, 5, 2, 1]

