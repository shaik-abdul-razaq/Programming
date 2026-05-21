result = []

for i in range(10, -6, -1):
    result.append(f"{i}@{i-1}")

print(",".join(result))