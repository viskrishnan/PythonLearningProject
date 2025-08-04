# r+ write and read

file = open('my_file.txt', 'r+')
written_data = file.write("Welcome! ")
print(written_data)
file.close()

file = open('my_file.txt', 'r+')
reading_data = file.read()
print(reading_data)
file.close()