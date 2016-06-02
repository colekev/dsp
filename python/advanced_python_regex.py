import csv
import re

with open('faculty.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    degrees = []
    titles = []
    emails = []
# Get degree, titles, emails
    for row in readCSV:
        degree = row[1]
        title = row[2]
        email = row[3]

        degrees.append(degree)
        titles.append(title)
        emails.append(email)
# find number of degrees and frequency
    for i in range(0,len(degrees)):
        degrees[i] = degrees[i].lstrip(' ') # remove space at beginning
        degrees[i] = re.sub('[0\.]', '', degrees[i]) # remove periods & '0'
        degrees[i] = re.split(' ', degrees[i])

    degrees = sum(degrees, [])

    from collections import Counter
    print(Counter(degrees)) # gives frequency of each degree

    print(Counter(titles)) # gives frequency of each titles



