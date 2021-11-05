if __name__ == '__main__':
    x = int(input()) 
    y = int(input())
    z = int(input())
    n = int(input())
    
# x, y, z are three dimensions of a cuboid
# n is an integer
# i+j+k != n 


i = [i for i in range (x+1)]
j = [j for j in range (y+1)]
k = [k for k in range (z+1)]

from math import factorial as fact

num_permut = fact(len(i)) * fact(len(j)) * fact(len(k))

permutations = []

for first in range(len(i)):
    for second in range(len(j)):
        for third in range(len(k)):
            if (n != first+second+third):           
                permutations.append([first, second, third])
                
print(permutations)
