'''Author: Santhosh Bheeman'''

print("Enter 1st string:")
str1=raw_input()
print("Enter 2nd string:")
str2=raw_input()

if str(sorted((str1))) == str(sorted((str2))):
    print("It is Anagram")
else:
    print("Not Anagram")
