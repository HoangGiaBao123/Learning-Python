x = 3
y = 3
z = 3
n = 3
result = []

for i in range(0, x + 1):
        for j in range(0, y + 1):
            for k in range(0, z + 1):
                if (i + j + k != n):
                    result.append([i, j, k])

print(result)