# data added to the file

# file = open('data.txt', 'a')
# content = '\nHelo Karthik kumar reddy '
# file.write(content)
# file.close()

# open file using  with method
#  with open('data.txt','r') as file:
#     contents =file.read()
#     print(contents)
#     file.close()


#  defference b/w readline and readlines
with open('data.txt','r') as file:
    # line1 =file.readline()
    # line2 = file.readline()
    lines = file.readlines()
    file.close()
print(lines)
for line in lines:
    print(line)