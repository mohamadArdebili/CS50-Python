s = input("Enter the File-name: ").lower()

if ".txt.pdf" in s:
    print("application/pdf")
elif ".gif" in s:
	print("image/gif")
elif ".jpg" in s:
	print("image/jpeg")
elif ".png" in s:
	print("image/png")
elif ".txt" in s:
	print("text/plain")
elif ".pdf" in s:
	print("application/pdf")
elif ".zip" in s:
	print("application/zip")
elif ".jpeg" in s:
	print("image/jpeg")
else:
	print("application/octet-stream")

