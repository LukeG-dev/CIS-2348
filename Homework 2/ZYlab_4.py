# Luke Gilin 1216992
# Zybooks 8.10 CIS 2348 LAB: Palindrome

text = input()
#  assign the text2 string with the reverse of the text string, removes spaces from test strings
text3 = text.replace(" ", "")
text2 = text3[::-1]

#  test if palindrome and print
if text3 == text2:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")