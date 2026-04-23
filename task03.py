r01 = open('Input/numbers.txt', 'r')

data = r01.read()
result = data.split()
max_num = int(result[0])
for num in result:
    if int(num) > max_num:
        max_num = int(num)

output_result = open('Output/output03.txt', 'w')
output_result.write(str(max_num))
