fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
print(fruits.count('apple'))
fruits.count('tangerine')
print(fruits.count('tangerine'))
fruits.index('banana')
print(fruits)
fruits.index('banana', 4)  # Find next banana starting at position 4
print(fruits)
fruits.reverse()
print(fruits)
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
print(fruits)
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
print(fruits)
fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
'pear'
print(fruits)

stack = [3, 4, 5]
print(stack)
stack.append(6)
print(stack)
stack.append(7)
print(stack)
stack
[3, 4, 5, 6, 7]
stack.pop()
7
print(stack)
stack
[3, 4, 5, 6]
print(stack)

stack.pop()
6
print(stack)
stack.pop()
5
print(stack)
stack
[3, 4]
print(stack)