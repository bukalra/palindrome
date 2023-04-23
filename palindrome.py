def is_palindrome(data):
    if not isinstance(data, str):
        return False
    data = data.lower()
    return data == data[::-1]