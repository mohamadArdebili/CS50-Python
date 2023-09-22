from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()
    test_wrong_values()
def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_wrong_values():
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

if __name__=="__main__":
    main()
