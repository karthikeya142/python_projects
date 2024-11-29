marks = int(input('Enter Marks '))
# >90 a,>70 b, >60 c, <60 d
if marks>90:
    print(f'Grade A {marks}')
elif marks>70:
    print(f'Grade B {marks}')
elif marks>60:
    print(f'Grade C {marks}')
elif marks<60:
    print(f'Grade D {marks}')
