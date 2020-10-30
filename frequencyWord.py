# Design a program to count frequency of occurence of word in a given sentence or string input

str_input = input()

def myFunc(str_input):
  # break the string input into words
  str_input = str_input.split()
  str_input2 = []

  for i in str_input:
    if i not in str_input2:
      str_input2.append(i)
  
  for i in range(0, len(str_input2)):
    print("Frequency of ", str_input2[i], " is: ", str_input.count(str_input2[i]))

# Invoke my main function to execute the program
myFunc(str_input)
