file_input = input("please, iput your file name: ").lower().strip()
if file_input.endswith(".gif"):
    print("image/gif")
elif file_input.endswith(".jpg") or file_input.endswith(".jpeg"):
    print("image/jpeg")
elif file_input.endswith(".png"):
    print("image/png")
elif file_input.endswith(".pdf"):
    print("application/pdf")
elif file_input.endswith(".txt"):
    print("text/plain")
elif file_input.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")