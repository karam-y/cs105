#Discretize the attribute Grade, also cleanup data
f = open('student-mat.csv','r')
outf = open('DisStudentGrade.csv','w')

header = f.readline() #Skip header
newheader = ','.join(header.split(';'))
print(newheader[:-1], file = outf)

for line in f:
    line = line.replace('"',"") #Remove quotes 
    newline = line[:-1].split(';') #Remove \n and split into an index
    if int(newline[-1]) <= 9:
        newline[-1] = 'F'
    elif int(newline[-1]) >= 10 and int(newline[-1]) <= 11:
        newline[-1] = 'D'
    elif int(newline[-1]) >= 12 and int(newline[-1]) <= 13:
        newline[-1] = 'C'
    elif int(newline[-1]) >= 14 and int(newline[-1]) <= 15:
        newline[-1] = 'B'
    else:
        newline[-1] = 'A'
    joinline = ','.join(newline)
    print(joinline,file = outf)
    
f.close()
outf.close()
