# Problem:

#     A set is an unordered collection of elements 
#     without duplicate entries. When printed, iterated or converted 
#     into a sequence, its elements will appear in an arbitrary order.

def average(array):
    
    unq = list(set(array))
    
    return sum(unq)/len(unq)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)