import re

string = input("\nInput something: ")

letters = ''.join([i for i in string if not i.isdigit()])

numArray = re.findall(r'\d+', string)
numArray = [int(i) for i in numArray]

print("\nRow without numbers:", letters)
print("Array of numbers:", numArray)

stringRow = ' '.join(word[0].upper() + word[1:-1] + word[-1:].upper() for word in letters.split())
print("\nRow with letters:", stringRow)
print("Max element of array of numbers:", max(numArray))

numArray.remove(max(numArray))
numArrayEl_Index = [numArray[i]**i for i in range(0,len(numArray))]
print("Array of numbers, elevated to degree by their index:", numArrayEl_Index)
print("\n")
