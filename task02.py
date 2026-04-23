r01 = open('Input/numbers.txt', 'r')

data = r01.read()
result = data.split()
s = 0
for num in result:
    s += int(num)

output_result = open('Output/output02.txt', 'w')
output_result.write(str(s))

