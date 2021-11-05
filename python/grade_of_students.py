# Problem:
#        Given the names and grades for each student in a class of  students,
#        store them in a nested list and print the name(s) of any student(s) 
#        having the second lowest grade.
#        Note: If there are multiple students with the second lowest grade, 
#        order their names alphabetically and print each name on a new line.

def sort_list(l):         # it will sort the list ascending according to the score
    l.sort(key = lambda x: x[1])
    return l
def find_min(l):
    return l[0][1]

def find_min2(l, min_val):
    for i, val in enumerate(l):
        if val[1]>min_val:
            min_val2 = val[1]
            break
    return min_val2

def find_student(l, min_val2):
    target = []
    for i, val in enumerate(l):
        if val[1] == min_val2:
            target.append(val[0])
    return sorted(target)

records = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

sorted_records = sort_list(records)
min_val = find_min(sorted_records)
min_val2 = find_min2(sorted_records, min_val)
students = find_student(sorted_records, min_val2)
for std in students:
    print(std)

    
