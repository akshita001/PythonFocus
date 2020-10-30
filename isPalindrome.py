# check for if word is a palindrome or not

def isPalindrome(word_input):
  return word_input == word_input[::-1]

word_input = input()
response = isPalindrome(word_input)

if response:
  print("yes, input word is a palindrome")
else:
  print("no, input word is not a palindrome")
