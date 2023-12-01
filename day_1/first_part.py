f = open("day_1/data.txt", "r")

total_sum = 0
numbers = []

for line in f:
    digits = [char for char in line if char.isdigit()]
    if digits:
        first_digit = digits[0]
        last_digit = digits[-1]
        num = int(first_digit + last_digit)
        numbers.append(num)

print(numbers)

# Sum all numbers in list
for number in numbers:
    total_sum += number

print(total_sum)

f.close()
            

          

            
            
        
    