numbers = [1,2,3,4,5,6,7,8,9,10]
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n %i ==0:
            return False
    return True

def get_input():
    try:
        n = int(input("Enter the number of values: "))
        values = [int(input(f"Enter value {i+1}: ")) for i in range(n)]
        return values
    except ValueError:
        print("Invalid input! Please enter integers only.")
        return get_input()

def filter_primes(values):
    return list(filter(is_prime, values))

# Get user input
values = get_input()


prime_list = list(filter(is_prime, values))
print(prime_list)