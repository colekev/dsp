import csv
import re

with open('faculty.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    names = []
    degrees = []
    titles = []
    emails = []
    lastNames = []
    firstNames = []
    info = []
# Get degree, titles, emails
    for row in readCSV:
        name = row[0]
        degree = row[1].lstrip(' ') # remove space at beginning
        title = row[2]
        email = row[3]

        names.append(name)
        degrees.append(degree) # remove space at beginning
        titles.append(title)
        emails.append(email)
        lastNames.append(name.split()[-1])
        firstNames.append(name.split()[0])

        info.append([degree] + [title] + [email])


    lastNames = lastNames[1:len(lastNames)]
    info = info[1:len(info)]

    from collections import defaultdict

    faculty_dict = defaultdict(list)

    for i in range(0, len(lastNames)):
        faculty_dict[lastNames[i]].append(info[i])

    for key in sorted(faculty_dict)[:3]:
        print('%s: %s' % (key, faculty_dict[key])) # Q6 answer
# Split names
    firstNames = firstNames[1:len(lastNames)]
    lastFirst = list(zip(firstNames, lastNames))

    professor_dict = defaultdict(list)

    for i in range(0, len(lastFirst)):
        professor_dict[lastFirst[i]].append(info[i])

    for key in sorted(professor_dict)[:3]:
        print('%s: %s' % (key, professor_dict[key])) # Q7 answer

        for key in sorted(professor_dict, key = lambda x: x[1])[:3]:
        print('%s: %s' % (key, professor_dict[key])) # Q8 answer sorted by last name


