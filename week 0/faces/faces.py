
def convert(string_user):
    emoji_string = string_user.replace(":)" , "🙂")
    emoji_string2 = emoji_string.replace(":(" , "🙁")
    return (emoji_string2)

def main():
    i = input("Write me the sentence: ")
    user_string = convert(i)
    print(user_string)

main ()
