
s = input("Enter the string: ")
vowels = ["a", "e", "i", "o", "u" , "A", "E", "I", "O", "U"]
new_s = ""
for c in range(len(s)):
    if s[c] not in vowels:
        new_s += s[c]

print (new_s)