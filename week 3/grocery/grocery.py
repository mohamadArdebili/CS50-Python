# grocery {"item" : "number"}
grocery={}
while True:
    try:
        item = input().upper().strip()
        if item not in grocery:
            grocery[item] = 1
        elif item in grocery:
            grocery[item] += 1

    except EOFError:
        for item in sorted(grocery):
            print ( grocery[item] ,item)
        break
