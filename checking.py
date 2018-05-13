def page_count_one(n, p):
    return min(p//2, n//2 - p//2)

def page_count_two(n, p):
    mid_point = n // 2
    if p <= mid_point:
        return (p // 2)
    if p > mid_point:
        distance = n - p
        return (distance // 2)

for n in range(1, 101):
    for p in range(1, n+1):
        res_one = page_count_one(n, p)
        res_two = page_count_two(n, p)
        if res_one != res_two:
            print("N:", n)
            print("P:", p)
            print("result one", res_one)
            print("result two", res_two)
