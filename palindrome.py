def palindrome(word):
    reverse = word[::-1]
    if word == reverse:
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is NOT a palindrome.")

