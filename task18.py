r01 = open('Input/students.txt', 'r')

result = r01.read()
students = result.split()

wanted_student = input("Ism kiriting: ")

if wanted_student in students:
    result = f"{wanted_student} found"
else:
    result = f"{wanted_student} not found"


output_result = open('Output/output18.txt', 'w')
output_result.write(str(result))