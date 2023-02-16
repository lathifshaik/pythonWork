def main():
    s = input("File name: ")
    s = s.lower()
    if ".gif" in s :
        print("image/gif")
    elif ".jpg" in s or ".jpeg" in s:
        print("image/jpeg")
    elif ".png" in s:
        print("image/png")
    elif ".pdf" in s:
        print("application/pdf")
    elif ".txt" in s:
        print("text/plain")
    elif ".zip" in s:
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()