from seasons import date_test

def main():
    test_date_test()

def test_date_test():
    assert date_test('2023-08-07') == ("2023 8 7")
    assert date_test("1998-02-10") == ("1998", "2", "10")
    assert date_test("February 6th, 1998") == None

if __name__ == "__main__":
    main()
