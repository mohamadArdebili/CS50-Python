from um import count

def main():
    test_count_1()
    test_count_2()
    test_count_3()

def test_count_1():
    assert count("um") == 1

def test_count_2():
    assert count("um, um, yummy") == 2

def test_count_3():
    assert count("Um, thanks for album") == 1
    assert count("hello, world") == 0
    
if __name__ == "__main__":
	main()