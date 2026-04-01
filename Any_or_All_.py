if __name__  == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    is_positive = all(num >= 0 for num in nums)
    is_palindromic = any("".join(reversed(str(num))) == str(num) for num in nums)
    if is_palindromic and is_positive:
        print("True")
    else:
        print("False")
