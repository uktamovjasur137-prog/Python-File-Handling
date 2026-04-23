r01 = open('Input/students.txt', 'r')

result = r01.read()
students = result.split()

sorted_students  = filter(lambda x: x.startswith('A'), students)

output_result = open('Output/output17.txt', 'w')
output_result.write(str(list(sorted_students)))