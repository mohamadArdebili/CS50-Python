from plates import is_valid

def main():
    test_min()
    # test_2_chars()
    # test_max_min()
    # test_num()
    # test_punctuation()

def test_min():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("awdgubobdad") == False
"""
def test_2_chars():
    assert is_valid("c") == False
    assert is_valid("hello, world") == False
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == False
    assert is_valid("c50000") == False
    assert is_valid("5") == False
def test_max_min():
    assert is_valid("23") == False
    assert is_valid("cs") == True
    assert is_valid("OUTATIME") == False
def test_num():
    assert is_valid("cs.,32") == False
    assert is_valid("CS50P2") == False
    assert is_valid("CS32") == True
def test_punctuation():
    assert is_valid("cs05") == False
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
"""
if __name__ == "__main__":
    main()

