#Q2
import string

filename = input("Enter the name of the text file: ")
with open(filename, encoding='utf-8') as file:
    text = file.read()

sentences = text.count('.')
words = text.split()

punctuations = string.punctuation
sentence_lengths = []
for sentence in text.split('.'):
    length = len(sentence.translate(str.maketrans("", "", punctuations)).split())
    if length > 0:
        sentence_lengths.append(length)
avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths)

vocabulary = set(words)

print(f"Number of sentences: {sentences}")
print(f"Number of words: {len(words)}")
print(f"Average length of sentences: {avg_sentence_length}")
print(f"Vocabulary size: {len(vocabulary)}")
