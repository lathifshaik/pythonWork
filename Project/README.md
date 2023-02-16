# Qrcode geneator
#### Video Demo: https://youtu.be/28wGJ9rrVFY
#### Description:
The basic view of this cs50P finel project is to make Qrcodes out of  urls
i desinged this project by using 3 fuctions

the libraries used in this project
import pyqrcode
import png
from pyqrcode import QRCode
import re
import sys


def get_data():
    url = input("Enter Url: ")
    return url

this function is used to get the data from the function

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

i used regular expresions to validate the
url wheather it is valid if its valid
then the fuction returns true

def Qrcode(url):
    url = pyqrcode.create(url)
    # Create and save the png file naming "myqr.png"
    url.png('myqr.png',scale = 15)
    return True

then we created this Qrcode function using the
pyqrcode libeary which gives us
the advanate to build a qrcode

url = get_data()
    # Generate QR code
    if(isValidURL(url) == True):
        Qrcode(url)

        print("Your QR has created")

    else:
        sys.exit('Not a Valid address')

this main funtion get's the data from functions
if qr created it "Your QR has created" else
it exists with 'Not a Valid address' using sys


Testing program::

from project import isValidURL,Qrcode

def main():
    test_function_1()
    test_function_2()
    test_function_n()


def test_function_1():
    assert isValidURL('abcdef') == False
    assert isValidURL('https://ide.cs50.io/bd9ce2f9989e42d7a1744134a84ac6b4') == True
    assert isValidURL('https://www.google.com/search?q=ashique+2&oq=ashique+2&aqs=chrome') == True
    assert isValidURL('https://cs50.harvard.edu/python/2022/project/') == True




def test_function_2():
    assert Qrcode('https://ide.cs50.io/bd9ce2f9989e42d7a1744134a84ac6b4') == True
    assert Qrcode('https://cs50.harvard.edu/python/2022/project/') == True


def test_function_n():
    assert isValidURL('https://www.google.com/search?q=ashique+2&oq=ashique+2&aqs=chrome') == True
    assert isValidURL('https://cs50.harvard.edu/python/2022/project/') == True



if __name__ == "__main__":
    main()


our testing program tests all the functions in project file
and i have taken some example urls


