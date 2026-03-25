def average(arr):
    setted_arr = set(arr)
    return sum(setted_arr) / len(setted_arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
