# # A palindrome is a word or phrase that can be read the same way backward or forward,
# # as with the words redivider, kayak, and civic.
#
word = input()
def palindrom():
    palindrome_flag = True
    for i in range(0, int(len(word)/2)):
        if word[i] != word[len(word)-i-1]:
            palindrome_flag = False
        else: palindrome_flag = True

    if palindrome_flag:
        print(f'this is a palindrome string')
    else: print(f'this is not a palindrome string')

palindrom()

# function which return reverse of a string

# def isPalindrome(s):
# 	return s == s[::-1]
#
#
# # Driver code
# s = "karthik"
# ans = isPalindrome(s)
#
# if ans:
# 	print("Yes")
# else:
# 	print("No")
