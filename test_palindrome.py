from palindrome import is_palindrome

def test_palindrome(test_value):
    try:
        assert is_palindrome(test_value)
    except ValueError:
        pass

if __name__ == '__main__':
    for test_value in ['kajak', 'oko', 'test', 'ala ma kota', 'a', '', '  ']:   
        print(f'{test_palindrome.__name__}: "{test_value}"', end=' ')
        try:
            test_palindrome(test_value)
            print('is a palindrome!')
        except AssertionError as error:
            print("it is not a palindrome!")