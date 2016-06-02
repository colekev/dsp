import csv
import re

with open('faculty.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    degrees = []
    titles = []
    emails = []
# Get degree, titles, emails
    for row in readCSV:
        email = row[3]

        emails.append(email)

    emailList = emails[1:len(emails)] # gets rid of header

with open('email.csv', 'w', newline = '') as file:
    email = csv.writer(file)
    for i in emailList:
        email.writerow([i])

