f01 = open('input.txt', 'r')
data = f01.read()

result = data.title()

f02 = open('output.txt', 'w')
f02.write(result)
