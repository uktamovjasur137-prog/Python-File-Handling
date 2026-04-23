r01 = open('Input/numbers.txt', 'r')

result = r01.read()

output_result = open('Output/output01.txt', 'w')
output_result.write(result)