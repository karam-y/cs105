'''
This program takes in our dataset student-mat.csv that has the format "a";"b";"c" and turns
it into a,b,c and also gets rid of a number of unneccessary attributes such as G1 (period 1), G2 (period 2),
school, mother's and father's jobs, guardian, family size, reason for picking school, and nursery school.
Saves it as CleanedData.csv
'''

f = open('student-mat.csv','r')
outf = open('CleanedData.csv','w')

header = f.readline() #Skip header
newheader = header[:-1].split(';')
newheader = newheader[1:8] + newheader[12:19] + newheader[20:30] + newheader[-2:-1]
joinheader = ','.join(newheader)
print(joinheader[:-1], file = outf)

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
        
    line = newline[1:8] + newline[12:19] + newline[20:30] + newline[-1:]
    
# change Medu from numeric to nominal
    if line[5] == '0':
        line[5] = "none"
    elif line[5] == '1':
        line[5] = "elementary"
    elif line[5] == '2':
        line[5] = "junior high"
    elif line[5] == '3':
        line[5] = "high school"
    else:
        line[5] = "college"

# change Fedu 
    if line[6] == '0':
        line[6] = "none"
    elif line[6] == '1':
        line[6] = "elementary"
    elif line[6] == '2':
        line[6] = "junior high"
    elif line[6] == '3':
        line[6] = "high school"
    else:
        line[6] = "college"
    
# change traveltime
    if line[7] == '1':
        line[7] = "<15 min"
    elif line[7] == '2':
        line[7] = "15 to 30 min"
    elif line[7] == '3':
        line[7] = "30 min to 1 hr"
    else:
        line[7] = ">1 hour"

# change studytime
    if line[8] == '1':
        line[8] = "<2 hours"
    elif line[8] == '2':
        line[8] = "2 to 5 hours"
    elif line[8] == '3':
        line[8] = "5 to 10 hours"
    else:
        line[8] = "10 hours"

# change famrel
    if line[17] == '1':
        line[17] = "very bad"
    elif line[17] == '2':
        line[17] = "bad"
    elif line[17] == '3':
        line[17] = "average"
    elif line[17] == '4':
        line[17] = "good"
    else:
        line[17] = "excellent"

# change freetime
    if line[18] == '1':
        line[18] = "very low"
    elif line[18] == '2':
        line[18] = "low"
    elif line[18] == '3':
        line[18] = "average"
    elif line[18] == '4':
        line[18] = "high"
    else:
        line[18] = "very high"

# change goout
    if line[19] == '1':
        line[19] = "very low"
    elif line[19] == '2':
        line[19] = "low"
    elif line[19] == '3':
        line[19] = "average"
    elif line[19] == '4':
        line[19] = "high"
    else:
        line[19] = "very high"

# change Dalc
    if line[20] == '1':
        line[20] = "very low"
    elif line[20] == '2':
        line[20] = "low"
    elif line[20] == '3':
        line[20] = "average"
    elif line[20] == '4':
        line[20] = "high"
    else:
        line[20] = "very high"

# change Walc
    if line[21] == '1':
        line[21] = "very low"
    elif line[21] == '2':
        line[21] = "low"
    elif line[21] == '3':
        line[21] = "average"
    elif line[21] == '4':
        line[21] = "high"
    else:
        line[21] = "very high"

# change health
    if line[22] == '1':
        line[22] = "very bad"
    elif line[22] == '2':
        line[22] = "bad"
    elif line[22] == '3':
        line[22] = "average"
    elif line[22] == '4':
        line[22] = "good"
    else:
        line[22] = "very good"
        
    line = ','.join(line)
    print(line, file = outf)
    
f.close()
outf.close()
