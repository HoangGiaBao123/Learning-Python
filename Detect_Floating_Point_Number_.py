def is_float(strg):
    if not "." in strg or strg.count(".") >= 2:
        return False
    try:
        float(strg)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    T = int(input())
    for t in range (0, T):
        S = input()
        print(is_float(S))
