words = input('Input Sentence:')

x = 0
completeList = []   #define variables to


for letter in words:
    if x%2 ==0:
        upperLetter = letter.upper()
        completeList.append(upperLetter)
    else:
        completeList.append(letter)
    x +=1
    s = ''.join(completeList)

print(s)
#only works in python
