import re

# https://www.youtube.com/embed/xvFZjo
# replace with "https://youtu.be/"

s = input("HTML: ").strip()
e = re.search(r"\"?https?://(www\.)?youtube\.com/embed/(.+)",s, re.IGNORECASE)
if e:
    split = (e.group(2)).split('"')
    url = split[0]
    print ("https://youtu.be/"+url)

# <iframe with= width="560" src="http://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube></iframe>
