r01 = open('Input/numbers.txt', 'r')

data = r01.read()
numbers = data.split()

total = 0
for num in numbers:
    total += int(num)

avg = total / len(numbers)
    
    

output_result = open('Output/output05.txt', 'w')
output_result.write(str(avg))