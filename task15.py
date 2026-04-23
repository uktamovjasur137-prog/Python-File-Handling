r01 = open('Input/students.txt', 'r')

result = r01.read()
students = result.split()

sorted_students  = {}
for student in students:
    sorted_students[student] = len(student)


output_result = open('Output/output15.txt', 'w')
output_result.write(str(sorted_students))