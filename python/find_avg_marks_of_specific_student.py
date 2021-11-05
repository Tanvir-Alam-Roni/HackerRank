# Problem:

#      The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
    def find_avg(record, key):
        return sum(record[key])/len(record[key])
        
    
avg_score = find_avg(student_marks, query_name)
    
    
print ('%.2f'%avg_score)
     
    
    
    
    
    
