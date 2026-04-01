if __name__ == '__main__':
    countries = []
    n = int(input())
    for i in range(1, n + 1):
        country = input()
        countries.append(country)
    print(len(set(countries)))
