#The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

with open('football.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    goals = []
    goalsAll = []
    teams = []
    for row in readCSV:
        team = row[0]
        goal = row[5]
        goalAll = row[6]

        teams.append(team)
        goals.append(goal)
        goalsAll.append(goalAll)

    n = len(goals) - 1
    goalDiff = []
    for i in range(1,n):
        diff = abs(int(goals[i]) - int(goalsAll[i]))
        goalDiff.append(diff)

    teamIndex = (goalDiff.index(min(goalDiff))) + 1
    teamMinDiff = teams[teamIndex]

    print(teamMinDiff)
