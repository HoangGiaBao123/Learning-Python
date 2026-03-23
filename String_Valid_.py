def is_alphanumeric(s):
    return any(char.isalnum() for char in s)

def is_alphabetical(s):
    return any(char.isalpha() for char in s)
    
def is_digit(s):
    return any(char.isdigit() for char in s)
    
def is_lower(s):
    return any(char.islower() for char in s)
    
def is_upper(s):
    return any(char.isupper() for char in s)

if __name__ == '__main__':
    s = input()
    print(is_alphanumeric(s))
    print(is_alphabetical(s))
    print(is_digit(s))
    print(is_lower(s))
    print(is_upper(s))
