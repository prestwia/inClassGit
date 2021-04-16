def divisors(a):
    results = []
    for i in range(1, a):
        if a % i == 0:
            results.append(i)
    return results




    
            