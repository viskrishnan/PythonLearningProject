user_text = input("Enter text to write to the file: ")
with open('output.txt', 'w') as f:
    print(user_text, file=f)
    print("Data successfully written to output.txt")
    f.close()

additional_user_text = input("Enter additional text to append: ")
with open('output.txt', 'a') as f:
    print(additional_user_text, file=f)
    print("Data successfully written to output.txt")
    f.close()

file = open('output.txt','r')
print("Final content of output.txt:")
print(file.read())
file.close()



"""
user_text = input("Enter text to write to the file: ")
file = open('output.txt', 'w')
file.write(user_text)
print("Data successfully written to output.txt")
file.close()

additional_user_text = input("Enter additional text to append: ")
file = open('output.txt', 'a')
file.write(additional_user_text)
print("Data successfully appended")
file.close()

file = open('output.txt','r+')
print("Final content of output.txt:\n")
print(file.read())
file.close()
"""