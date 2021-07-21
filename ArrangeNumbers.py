
print("Q2 starts:        ")
print("==================")
print()
print()

n = input("Enter Number: ")

def ascendingNumber(n):
    number = str(n)
    number = ''.join(sorted(number))
    number = int(number)
    return number

print("After reordering: ",ascendingNumber(n))


print()
print()
print("Q2 ends:          ")
print("==================")
