if __name__ == '__main__':
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    n = int(input())
    words = input().strip().split()
    score = 0
    for i in range(0, n):
        v = [c for c in words[i] if c in vowels]
        if len(v) % 2 == 0:
            score = score + 2
        else:
            score = score + 1
    print(score)
