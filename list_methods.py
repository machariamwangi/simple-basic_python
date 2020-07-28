numbers = [2, 5, 6, 5, 7, 20]
numbers.append(22)
numbers.insert(0, 34)
numbers.remove(5)
numbers.pop()
print(numbers.index(6))
print (50 in numbers)
print(numbers.count(5))
# numbers.clear() ===> clears everything in a loop
print(numbers)

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers2  = numbers.copy()
numbers.append(10)
print(numbers)
print(numbers2)