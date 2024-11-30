import string

# List of symbols to map to each ASCII character (printable range only)
symbols = [chr(i) for i in range(33, 127)]

# Manually set the space to map to "__" and assign the rest
coder_dict = {" ": "__"}
coder_dict.update({char: symbols[i] for i, char in enumerate(string.printable[1:-6])})

# Print the dictionary
print(coder_dict)
