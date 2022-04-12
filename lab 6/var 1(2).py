

numbers = [5,2,8,6,11,52,53,51,0,7,2,0,9,8]
average = sum(numbers) / len(numbers)
numbers = [average if i == 0 else i for i in numbers]

print(numbers)