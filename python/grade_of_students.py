# Problem:
#        Given the names and grades for each student in a class of  students,
#        store them in a nested list and print the name(s) of any student(s) 
#        having the second lowest grade.
#        Note: If there are multiple students with the second lowest grade, 
#        order their names alphabetically and print each name on a new line.



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

    
