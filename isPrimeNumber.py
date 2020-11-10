# check for prime number or based on user input
# user can enter a number and program should be able to check and provide an out put whether it is a prime number or not

n = int(input())
# if input number is greater than 1
if n > 1:
  #iterate from 2 to n/2
  for i in range(2, n):
    # if no is divisible by any no between 2 and n/2, it is not prime
    if (n % i) == 0:
      print("The number: ", n , "is not a prime number")
      break
  else:
    print("The number: ", n," is a prime number")
else:
  print("The number: ", n , " is not a prime number")
