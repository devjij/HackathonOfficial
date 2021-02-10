# This is a sample Python script.

sentence = input("Please enter a sentence to encode:\n")
# asks for sentence and sets input equal to variable sentence

str_length = len(sentence)
# determines number of characters in string

x = 0
while x != str_length:
    newCharacter = ord(sentence[x])
    x = x + 1
    print(newCharacter)


print("This projects for Hackathon")
print("This is a project made by Dev Jijilal, Sam Elmore, Jacob Chamoun, and Ian Corbett")

