
file1 = open('my_file.txt', 'w')
written_file = file1.write("Welcome")
file1.close()

file1 = open('my_file.txt', 'a')
file1.write(", Hello Ivaan")
file1.close()

file1 = open('my_file.txt', 'r')
reading_file = file1.read()
print(reading_file)
file1.close()