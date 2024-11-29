def luhn_check(card_number):
    card_number = str(card_number)
    total_sum = 0

    # Start from the end and move left
    for i, digit in enumerate(reversed(card_number)):
        n = int(digit)
        # Double every second digit
        if i % 2 == 1:
            n *= 2
            # print(f"i:" + i)
            # If the result is greater than 9, subtract 9
            if n > 9:
                n -= 9
                # print(f"n:"+ n)
        total_sum += n
        print(total_sum)

    # Check if the total sum is a multiple of 10
    return total_sum % 10 == 0


# Example usage:
card_number = input("Enter card: ") #"4592000224092722"
if luhn_check(card_number):
    print(f"{card_number} is a valid card number.")
else:
    print(f"{card_number} is not a valid card number.")

# card_no ="4592000224092722"
# odd_sum =0
# even_sum =0
# double_list =[]
# number= list(card_no)
# for (idx, val) in enumerate(number):
#     # print(str(idx)+" => "+val)
#     if idx % 2 != 0: # this is odd number
#         # print(val)
#         odd_sum += int(val)
#     else: # this is even value
#         double_list.append(int(val)*2)
#
# #convert the list string
# double_string = ""
# for x in double_list:
#     double_string += str(x)
#
# double_list =list(double_string)
# for x in double_list:
#     even_sum +=int(x)
# net_sum = odd_sum + even_sum
# if net_sum %10 == 0:
#     print("valid card")
# else:
#     print("invalid card")