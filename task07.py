r01 = open('Input/numbers.txt', 'r')

data = r01.read()
result = data.split()

nums =[]
for num in result:
    kvadrat = int(num) ** 2
    nums.append(kvadrat)
    

output_result = open('Output/output07.txt', 'w')
output_result.write(str(nums))