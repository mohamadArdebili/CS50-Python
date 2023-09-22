import inflect
p = inflect.engine()
# test_list.append(test_str)

name_list = []
while True:
    try:
        s = input("Input: ")
        name_list.append(s)
        names = p.join(name_list)
    except EOFError:
        print(f"Adieu, adieu, to {names}")
        break
