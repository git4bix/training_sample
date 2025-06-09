def remove_duplicates(numbers):
    for num in numbers:
        if numbers.count(num) > 1 :
            numbers.remove(num)
    return numbers

numbers = [1, 2, 2, 3, 3, 4]
print(f"Unique numbers: {remove_duplicates(numbers)}")