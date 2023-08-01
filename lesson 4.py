### OPERATORS

addition = 1 + 2
subtraction = 3 - 4
multiplication = 5 * 6
division = 7 / 8
modulus = 5 % 2
exponential = 9 ** 10
floor =  5 // 2

## Slices
someList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
### list[start:end:step]
print(someList[6])
print(someList[4:])
print(someList[6:8])
print(someList[2::2])
print(someList[:7:3])
print(someList[-1])
print(someList[::-1])
someWord = "frick"
print(someWord[0])
wordList = ["frick", "frack", "rfuck"]
print(wordList[0])



for number in someList:
    print(number)

for a in range(10):
    print("wow")
    
newList = []

for number in range(10):
    if number % 2 == 0:
        newList.append(number)

print(newList)

l = [x for x in range(10) if x % 2 == 0]
print(l)
