

# This is a sample Python script.

sentence = input("Please enter a sentence to encode:\n")
# asks for sentence and sets input equal to variable sentence

str_length = len(sentence)
# determines number of characters in string

digitsList = [0] * str_length
#determines how long the list should be based on length of sentence entered.
# Fills in all spots with 0's as placeholder

x = 0
while x < str_length:
    newCharacter = ord(sentence[x])
    digitsList[x] = int(newCharacter)
    #assigns space (known as x) in list to newly converted character
    x = x + 1

print("digits from original sentence converted to ASCII:")
print(*digitsList, sep=' ')
#prints sentence as ascii code

encodedList = digitsList
a = 0
while a < str_length:
    encodedList[a] = encodedList[a] * 3 + 34
    a = a + 1
#sample encoding process, multiplies numbers by 3 and adds 34

print("Encoded digits:")
print(encodedList)

print("FINAL Encoded sentence without spaces:")
print(*encodedList, sep='123562547')
#Places seperator of 123562547 between each converted letter, prints as one text block
