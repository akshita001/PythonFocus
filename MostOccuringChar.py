# Write a program to check Most Occurring Character and the Number of Occurrence of it

string = input("Enter string: ")

frequency_dict = {}

for character in string:
    if character in frequency_dict:
        frequency_dict[character] += 1
    else:
        frequency_dict[character] = 1

most_occurring = max(frequency_dict, key=frequency_dict.get)


print("Most Occuring character: ", most_occurring)
print("Number of Occurrence: %d " %(frequency_dict[most_occurring]))
