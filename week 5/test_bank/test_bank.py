from bank import value

def main():
    test_value1()
    test_value2()
    test_value3()
def test_value1():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello") == 0
    assert value("Hello there") == 0
def test_value2():
    assert value("hi") == 20
    assert value("hey there!") == 20
    assert value("How you doin") == 20
def test_value3():
    assert value("Welcome to the bank") == 100
    assert value("What's up!") == 100

if __name__=="__main__":
    main()