result = ""
q = int(input())

if q == 0:
    result = str(0)
else:
    while q:
        r = q % 2
        result = str(r) + result
        q //= 2
print(result)