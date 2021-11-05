def symm_diff(a, b):
    d1 = a.difference(b)
    d2 = b.difference(a)
    d = d1.union(d2)
    result = '\n'.join(sorted(d, key=int))
    return result

if __name__ == '__main__':
    m, arr1 = (int(input()), input().split())
    n, arr2 = (int(input()), input().split())
    set_a = set(arr1)
    set_b = set(arr2)
    
    result = symm_diff(set_a, set_b)
    print(result)
