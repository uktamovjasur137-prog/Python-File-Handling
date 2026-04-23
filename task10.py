r01 = open('Input/numbers.txt', 'r')

data = r01.read()
numbers = data.split()

nums = sorted(numbers, key=lambda x: int(x))

output_result = open('Output/output10.txt', 'w')
output_result.write(str(nums))