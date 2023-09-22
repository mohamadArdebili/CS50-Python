from numb3rs import validate

def main():
    test_true()
    test_false()

def test_true():
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("0.0.0.0") == True
def test_false():
    assert validate("512.512.512.512") == False
    assert validate("1.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
if __name__=="__main__":
	main()