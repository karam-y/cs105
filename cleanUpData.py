''' This program takes in our dataset student-mat.csv that has the format a;b;c and turns
it into a,b,c and also gets rid of the G1 (period 1) and G2 (period 2) columns and saves it
as student.csv
'''

infile = open('student-mat.csv','r')
outfile = open('student.csv','w')
for line in infile:
    line = line.replace(";",",")
    line = line.split(',')
    line = line[:30] + line[-1:]
    line = (',').join(line)
    print( line , file=outfile)
