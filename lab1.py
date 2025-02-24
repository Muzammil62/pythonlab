def is_palindrom(s):
    s=s.replace("","").lower()
    return s ==s[::-1]
word = input("Enter a word or phase:")
if is_palindrom(word):
    print(f"'{word}'is a palindrom.")
else:
    print(f"'{word}'is not a palindrom.")