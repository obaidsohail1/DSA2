# Define the recursive function to check if a word is a palindrome
de isPalindrome(word):
    # Base case: If the word has 0 or 1 character, it's a palindrome
    if len(word) <= 1:
        return True
    
    # Check the first and last characters
    if word[0] != word[-1]:
        return False  # Not a palindrome if the first and last characters differ
    
    # Recursively check the substring without the first and last characters
    return isPalindrome(word[1:-1])

# Test cases for the isPalindrome function
test_words = ["gag", "pop", "hannah", "rotator", "hello", "world"]

# Print the results for each test case
print("Palindrome Checker Results:")
for word in test_words:
    result = isPalindrome(word)
    print(f"{word}: {'Palindrome' if result else 'Not a Palindrome'}")
