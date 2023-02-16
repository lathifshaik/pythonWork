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