r01 = open('Input/numbers.txt', 'r')

data = r01.read()
result = data.split()

nums = []

for num in result:
    nums.append(f"{len(num)} xonali")

output_result = open('Output/output09.txt', 'w')
output_result.write(str(nums))