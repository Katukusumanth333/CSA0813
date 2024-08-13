#Alphabetic order
words = input("Enter words: ")
word_list = words.split()
word_list.sort()
print("Words in alphabetical order:")
for word in word_list:
    print(word)
