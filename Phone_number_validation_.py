def yes_or_no(S):
    if (len(S) == 10) and (S.isdigit()) and (S.startswith("7") or S.startswith("8") or S.startswith("9")):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        s = input()
        yes_or_no(s)
