while True:
        with open ('name.csv', 'a') as file:
                name = input(f' Enter name to be added: ')
                file.write(f'{name}\n' )
                choice = input(" do you want added more names? (y/n): ")
                if choice == 'n':
                   break

with open('name.csv', 'r') as file:
        lines = file.readlines()

for line in lines:
        print(line.strip().capitalize())