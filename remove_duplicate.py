numbers = [1, 4, 2, 7, 9, 10, 2, 6, 4]

unique_number = []

# Solution
# for number in numbers:
#     if numbers.count(number) >= 2:
#         numbers.remove(number)
# print(numbers)

# Corrections
for number in numbers:
    if number not in unique_number:
        unique_number.append(number)

print(unique_number)
