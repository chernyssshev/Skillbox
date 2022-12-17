from typing import List

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

results = map(lambda x, y: (x, y), letters, numbers)
print(list(results))

# Как один из вариантов
results = [(letters[i], numbers[i]) for i in range(0, min(len(letters), len(numbers)))]
print(results)
