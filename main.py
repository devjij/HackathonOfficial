

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
    digitsList[x] = newCharacter
    #assigns space (known as x) in list to newly converted character
    x = x + 1

print(*digitsList, sep='')
#prints sentence as code

print("This projects for Hackathon")
print("This is a project made by Dev Jijilal, Sam Elmore, Jacob Chamoun, and Ian Corbett")

