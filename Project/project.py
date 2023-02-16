import pyqrcode
import png
from pyqrcode import QRCode
import re
import sys

def main():
    # String which represents the QR code
    url = get_data()
    # Generate QR code
    if(isValidURL(url) == True):
        Qrcode(url)

        print("Your QR has created")

    else:
        sys.exit('Not a Valid address')


def get_data():
    url = input("Enter Url: ")
    return url





def Qrcode(url):
    url = pyqrcode.create(url)
    # Create and save the png file naming "myqr.png"
    url.png('myqr.png',scale = 15)
    return True




def isValidURL(str):

    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if (str == None):
        return False

    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False


if __name__ == "__main__":
    main()