from twttr import shorten
#import pytest

def main():
    test_shorten()

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("hello, WORLD") == "hll, WRLD"
    assert shorten("Twitter") == "Twttr"
    assert shorten("23") =="23"
    assert shorten("CS50") == "CS50"

if __name__ == "__main__":
    main()