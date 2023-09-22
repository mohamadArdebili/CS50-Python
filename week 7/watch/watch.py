import re
import sys

# https://youtube.com/embed/xvFZjo
# http://youtube.com/embed/xvFZjo
# https://www.youtube.com/embed/xvFZjo
# changes to "https://youtu.be/xvFZjo5PgG0"
def main():
    print(parse(input("HTML: ").strip()))

def parse(s):
    if s.startswith("<iframe"):
        embed = re.search(r"\"?https?://(www\.)?youtube\.com/embed/(.+)",s, re.IGNORECASE)
        if embed:
            split = (embed.group(2)).split('"')
            url = split[0]
            return "https://youtu.be/" + url
    else:
        return None
if __name__=="__main__":
    main()