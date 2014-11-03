my_numbers = [2, 8, 64, 16, 32, 4, 16, 8]
for numbers in my_numbers:
    times_used = my_numbers.count(numbers)
    if times_used >1:
        answer = "The list provided contains duplicate values!"
        break
    
    else:
        answer = "The list provided does not contain duplicate values!"

print answer

my_numbers = [2, 8, 64, 16, 32, 4, 16, 8]
my_numbers.sort()
for numbers in my_numbers:
    times_used = my_numbers.count(numbers)
    if times_used > 1:
        my_numbers.remove(numbers)

print my_numbers
