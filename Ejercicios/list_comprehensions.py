#Syntax of list comprehensions
#   [expression for item in iterable (condition)]
Lista =[i for i in range(1,1001) if i % 4 ==0 and i % 6 == 0 and i % 9 == 0 ]

print(Lista[:5])
#finding transpose of matrix
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose_matrix = [[row[i] for row in matrix] for i in range(2)]
print (transpose_matrix)
# Reverse each elements in a specified tuple
List = [string[::-1] for string in ('pollo', 'Canabis', '420')]
# Display the list
print(List)
# creation of two lists to represent keys and values
keys=[1, 2, 3, 4, 5, 6]
values = ['a','b','c','d','f','g']
# implementing dictionary comprehension
new_dict = { k:v for (k,v) in zip(keys, values)}
print(new_dict)
#Create a dictionary like list_comprehensions
new_dict = {x: x*3 for x in [6, 5, 4, 3, 2, 1]}
print(new_dict)