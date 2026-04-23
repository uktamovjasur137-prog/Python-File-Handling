r01 = open('Input/students.txt', 'r')

result = r01.read()
students = result.split()

total = len(students)

output_result = open('Output/output12.txt', 'w')
output_result.write(f'Studentlar soni : {total}')