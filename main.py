# This is a sample Python script.

sentence = input("Please enter a sentence to decode:\n")

str_length = len(sentence)

x = 0
while x <= str_length - 1:
    print(ord(sentence[x]))
    x = x + 1

print("This projects for Hackathon")
print("This is a project made by Dev, Sam and Jacob.")
