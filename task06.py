r01 = open('Input/numbers.txt', 'r')

data = r01.read()
result = data.split()

nums =[]
for num in result:
    if int(num) % 2 != 0:
        nums.append(num)
    

output_result = open('Output/output06.txt', 'w')
output_result.write(str(nums))