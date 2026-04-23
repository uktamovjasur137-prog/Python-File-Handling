r01 = open('Input/students.txt', 'r')

result = r01.read()

output_result = open('Output/output11.txt', 'w')
output_result.write(result)