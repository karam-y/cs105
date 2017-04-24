# gabrielle french, gjfrench@bu.edu

# this code changes numeric, non-binary data into nominal data

infile = open('DisStudentGrade.csv','r')
outfile = open('FinalStudentPer.csv','w')

# change Medu from numeric to nominal
for line in infile:
    if line[6] is 0:
        line[6] = "none"
    elif line[6] is 1:
        line[6] = "elementary"
    elif line[6] is 2:
        line[6] = "junior high"
    elif line[6] is 3:
        line[6] = "high school"
    else:
        line[6] = "college"

# change Fedu 
for line in infile:
    if line[7] is 0:
        line[7] = "none"
    elif line[7] is 1:
        line[7] = "elementary"
    elif line[7] is 2:
        line[7] = "junior high"
    elif line[7] is 3:
        line[7] = "high school"
    else:
        line[7] = "college"
    
# change traveltime
for line in infile:
    if line[8] is 1:
        line[8] = "<15 min"
    elif line[8] is 2:
        line[8] = "15 to 30 min"
    elif line[8] is 3:
        line[8] = "30 min to 1 hr"
    else:
        line[8] = ">1 hour"

# change studytime
for line in infile:
    if line[9] is 1:
        line[9] = "<2 hours"
    elif line[9] is 2:
        line[9] = "2 to 5 hours"
    elif line[9] is 3:
        line[9] = "5 to 10 hours"
    else:
        line[9] = "10 hours"

# change famrel
for line in infile:
    if line[18] is 1:
        line[18] = "very bad"
    elif line[18] is 2:
        line[18] = "bad"
    elif line[18] is 3:
        line[18] = "average"
    elif line[18] is 4:
        line[18] = "good"
    else:
        line[18] = "excellent"

# change freetime
for line in infile:
    if line[19] is 1:
        line[19] = "very low"
    elif line[19] is 2:
        line[19] = "low"
    elif line[19] is 3:
        line[19] = "average"
    elif line[19] is 4:
        line[19] = "high"
    else:
        line[19] = "very high"

# change goout
for line in infile:
    if line[20] is 1:
        line[20] = "very low"
    elif line[20] is 2:
        line[20] = "low"
    elif line[20] is 3:
        line[20] = "average"
    elif line[20] is 4:
        line[20] = "high"
    else:
        line[20] = "very high"

# change Dalc
for line in infile:
    if line[21] is 1:
        line[21] = "very low"
    elif line[21] is 2:
        line[21] = "low"
    elif line[21] is 3:
        line[21] = "average"
    elif line[21] is 4:
        line[21] = "high"
    else:
        line[21] = "very high"

# change Walc
for line in infile:
    if line[22] is 1:
        line[22] = "very low"
    elif line[22] is 2:
        line[22] = "low"
    elif line[22] is 3:
        line[22] = "average"
    elif line[22] is 4:
        line[22] = "high"
    else:
        line[22] = "very high"

# change health
for line in infile:
    if line[23] is 1:
        line[23] = "very bad"
    elif line[23] is 2:
        line[23] = "bad"
    elif line[23] is 3:
        line[23] = "average"
    elif line[23] is 4:
        line[23] = "good"
    else:
        line[23] = "very good"

print(line, file = outfile)

infile.close()
outfile.close()
