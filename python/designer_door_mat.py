# Problem:
#     Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

#     Mat size must be X. ( is an odd natural number, and  is  times .)
#     The design should have 'WELCOME' written in the center.
#     The design pattern should only use |, . and - characters.


# --> width, m  height, n
N, M = input().split()
N = int(N)
M = int(M)
s = ".|."
for i in range(N//2):
    print(((2*i+1)*s).center(M, "-"))
print('WELCOME'.center(M, "-"))
for i in range(N//2, 0, -1):
    print(((2*i-1)*s).center(M, "-"))


