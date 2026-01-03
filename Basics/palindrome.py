
text = input("Enter a word or phrase: ")
normalized = text.replace(" ", "").lower()
if normalized == normalized[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")