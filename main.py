def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

s = input("So'z kiriting: ")
if is_palindrome(s):
    print("So'z palindrom")
else:
    print("So'z palindrom emas")