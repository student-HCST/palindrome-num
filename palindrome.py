def is_palindrome(text):
    # Convert to lowercase and remove spaces and punctuation
    cleaned = ''.join(char.lower() for char in text if char.isalnum())

    # Compare the text with its reverse
    return cleaned == cleaned[::-1]


# Get input from the user
text = input("Enter a word or phrase: ")

if is_palindrome(text):
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
