from unittest import result


list = [[i for i in range(j, 13, 4)] for j in range(1, 5)]
print(list)
result = [[value, value + 4, value + 8] for value in range(1, 5)]
print(result)
