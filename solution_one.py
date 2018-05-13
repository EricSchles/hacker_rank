def get_factors(numbers):
    min_num = min(numbers)
    factors = []
    for i in range(1, min_num+1):
        factor_to_all = []
        for number in numbers:
            factor_to_all.append(number // i == number / i)
        if all(factor_to_all):
            factors.append(i)
    return factors


def check_factors(factors, numbers):
    final_factors = []
    for factor in factors:
        all_are_factors = []
        for number in numbers:
            all_are_factors.append(factor // number == factor / number)
        if all(all_are_factors):
            final_factors.append(factor)
    return len(final_factors)


def getTotalX(a, b):
    possible_factors = get_factors(b)
    return check_factors(possible_factors, a)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()