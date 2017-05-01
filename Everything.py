'''
This program takes in our dataset student-mat.csv that has the format "a";"b";"c" and turns
it into a,b,c and also gets rid of a number of unneccessary attributes such as G1 (period 1), G2 (period 2),
school, mother's and father's jobs, guardian, family size, reason for picking school, and nursery school.
Saves it as CleanedData.csv
'''

f = open('student-Mat.csv','r')
outf = open('Matstudent.csv','w')

header = f.readline() #Skip header
newheader = header[:-1].split(';')
joinheader = ','.join(newheader)
print(joinheader[:-1], file = outf)

for line in f:
    line = line.replace('"',"") #Remove quotes 
    line = line[:-1].split(';') #Remove \n and split into an index
    line = ','.join(line)
    print(line, file = outf)
    
f.close()
outf.close()

