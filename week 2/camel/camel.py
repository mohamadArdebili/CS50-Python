# preferredFirstName
s = input("Enter the fuckiiiing string: ")
for c in s:
    if c.isupper():
        s = s.replace(c , f"_{c}")
lowering = s.lower()
print(lowering)