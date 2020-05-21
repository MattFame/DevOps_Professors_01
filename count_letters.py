word=input(str("Enter a word: "))

dic={}
for i in word:
    dic[i]=dic.get(i,0)+1
print(dic)
  

# Count the number of each letter in a sentence.

# The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.
# Write a Python program that

# takes a sentence from the user,
# counts the number of each letter of the sentence,
# collects the letters/chars as a key and the counted numbers as a value in a dictionary.

# Output example:

# {'s': 2, 'r': 1, 't': 1, 'h': 1, ' ': 3, 'n': 1, 'i': 1, 'u': 1, 'o': 1, 'p': 1, '!': 1}

