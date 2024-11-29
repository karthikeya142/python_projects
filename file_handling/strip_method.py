#this stripp method is used to remove
# the white spaces or whitespace  characters from string from either side


text = "   Hello Karthikeya!   "
print(text)
# affter applied strip method there is no white spaces
striped_text =text.strip()
print(striped_text)

# left whitespace remove spaces
striped_text1 =text.lstrip()
print(striped_text1)

# right  whitespace remove spaces
striped_text2 =text.rstrip()
print(striped_text2)


with open('app_accessKeys.csv','r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())