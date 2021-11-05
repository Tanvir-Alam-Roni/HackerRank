def happiness(array, A, B):
    return sum([(i in A) - (i in B) for i in array])

if __name__ == '__main__':
    n, m = input().split()
    arr = list(input().split())
    a = set(input().split())
    b = set(input().split())
    result = happiness(arr, a, b)
    print(result)
    