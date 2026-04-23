r01 = open('Input/students.txt', 'r')

result = r01.read()
students = result.split()

sorted_students = sorted(students, key=lambda x: x, reverse=True)

output_result = open('Output/output14.txt', 'w')
output_result.write(str(sorted_students))