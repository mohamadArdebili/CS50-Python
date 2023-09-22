from plates import is_valid

def main():
    test_length()
    test_firstchars()
    test_nums()
    test_invalid()
    
def test_length():
    assert is_valid("AA") == True
    assert is_valid("cs500") == True
    assert is_valid("a") == False
    assert is_valid("abcO50") == True

def test_firstchars():
    assert is_valid("ab") == True
    assert is_valid("a1") == False
    assert is_valid("50cs") == False

def test_nums():
    assert is_valid("CS50P2") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("cs100") == True
    assert is_valid("cs001") == False

def test_invalid():
    assert is_valid("cs0.5") == False
    assert is_valid("abc de") == False
    assert is_valid("cs?") == False
if __name__ == "__main__":
    main()