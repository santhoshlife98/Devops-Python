'''Author: Santhosh bheeman'''

print("Enter 1st string:")
str1=raw_input()
print("Enter 2nd string:")
str2=raw_input()

if str(str1) == str(str2[::-1]):
    print("it is palindrome")
else:
    print("not a palindrome")
