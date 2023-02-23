#Q1:
inp = input("Enter a line of text: ")
list = {}
for char in inp:
    if char.isalpha():
        char = char.lower()
        list[char] = list.get(char, 0) + 1

with open("output.txt", "w") as f:
    for letter in list:
        f.write(f"The letter {letter} appears {list[letter]} time(s)\n")

