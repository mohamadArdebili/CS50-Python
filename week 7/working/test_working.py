from working import convert
import pytest

def test_format():
    with pytest.raises(ValueError):
         convert('09:00 AM - 7:00 PM')
    with pytest.raises(ValueError):
         convert('9:00AM to 7:00PM')

def test_convert():
    assert convert('09:00 AM to 3:00 PM') == '09:00 to 15:00'
    assert convert('03:11 AM to 8:59 AM') == '03:11 to 08:59'

def test_range():
    with pytest.raises(ValueError):
         convert('09:00 AM to 17:00 PM')
    with pytest.raises(ValueError):
         convert('09:60 AM to 07:00 PM')

if __name__ == '__main__':
    main()


from working import convert
import pytest

"""
def main():
    test_convert_1()
    test_convert_2()
    test_convert_3()
def test_convert_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("12:30 AM to 8:50 AM") == "00:30 to 08:50"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
def test_convert_2():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
def test_convert_3():
    # assert convert("9:60 AM to 5:60 PM") == "ValueError"
    # assert convert("9 AM - 5 PM") == "ValueError"
    # assert convert("09:00 AM - 17:00 PM") == "ValueError"
    with pytest.raises(SystemExit):
        convert("8:70 AM to 12:70 PM")
    # with pytest.raises(ValueError):
    #     convert("9AM to 8PM")
    with pytest.raises(SystemExit):
        convert("09:00 to 17:00")
    # with pytest.raises( ValueError , SystemExit):
    #     convert("9 AM - 5 PM")
    with pytest.raises(SystemExit):
        convert("09:00 AM - 17:00 PM")

if __name__ == "__main__":
    main()
"""