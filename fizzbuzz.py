# Problem solving - Conditional statements usage in Python

# Write a program that will take an user input number, display Fizz if it is divisble by 3,
# display Buzz if it is divisible by 5, display FizzBuzz if it is divisible by 15 (5 and 3 both)
# and finally displays the number itself if it neither falls into any of the above scenarios.

# define the function
def fizz_buzz():
  # take user input
  n = int(input())

  if (n % 3 == 0) and ( n % 15 != 0):
    print("Fizz")
  elif (n % 5 == 0) and (n % 3 != 0):
    print("Buzz")
  elif n % 15 == 0:
    print("FizzBuzz")
  else:
    print(n)

# Invoke the function
fizz_buzz()
