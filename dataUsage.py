#!usr/bin/python3

import os
import datetime
import color_it as c
from get_dates import getdates

start, end = getdates()


def days_between(startDate, tnow):
    """
    Define the number of days for the 1TB of data since startDate.

    startDate is a constant. tnow is today.
    """
    startDate = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    tnow = datetime.datetime.strptime(tnow, "%Y-%m-%d")
    return abs((tnow - startDate).days)


def readData():
    """
    Read the data from the dataUsed text file.

    startDate is a constant. tnow is today.
    """
    with open('dataUsed.txt', 'r') as fRead:
        for line in fRead:
            pass

        if line == '\n':
            return 0
        else:
            last = line.strip()[40:]
            dataYesterday = last.strip()
            return dataYesterday


def writeData():
    """
    Append the data to the dataUsed text file.

    startDate is a constant. Is today.
    """
    with open('dataUsed.txt', 'a') as f:
        f.write(tnow + ' - ' + "Data used: " + str(dataUsed) +
                ' - ' + "Data left: " + str(dataLeft) + '\n')


startDate = str(start)
tnow = str(datetime.date.today())
endDate = str(end)
lastDay = end + datetime.timedelta(days=1)
cStart = c.colors.bold + c.colors.bg.black + c.colors.fg.yellow
cEnd = c.colors.reset
totalNumDays = days_between(startDate, endDate)
numDays = days_between(startDate, tnow)
daysLeft = days_between(tnow, endDate)

os.system("clear")
dataUsed = int(input('Provide the data used thusfar in G-bytes: '))
dataLeft = 1024 - dataUsed
perCentUsed = (dataUsed / 1024) * 100

print('Today is: ', tnow, '\nStart date is: ', startDate,
      '\nEnd Date is: ', endDate, '\nTotal days in plan: ', cStart,
      totalNumDays, cEnd)
if numDays > totalNumDays:
    numDays = totalNumDays
print('Number of days since start: ', cStart, numDays, cEnd)
print('Days left in your plan is: ', cStart, daysLeft, cEnd)
print('Percentage of time since start: ', cStart,
      round((numDays * 100 / totalNumDays), 2), cEnd)
print('Percentage of 1024 GBytes used is: ', cStart, round(perCentUsed, 2), cEnd)
print('Your average usage per day is: ', cStart,
      round(dataUsed / numDays, 2), cEnd, 'Gigabytes')
print('Amount of data left is: ', cStart, dataLeft, cEnd, 'Gigabytes')
if daysLeft >= 0:
    print('You need to stay under: ', cStart, round(dataLeft / daysLeft, 2), cEnd,
          'Gigabytes per day to avoid additional cost\n\n')
else:
    print('Yesterday was the last day of the plan!!')

dataYesterday = readData()

if dataYesterday is None:
    dataYesterday = 0
    dataUsedYesterday = dataUsed
else:
    dataUsedYesterday = int(dataYesterday) - dataLeft

print('You used: ', cStart, c.colors.underline, dataUsedYesterday, cEnd,
      ' GBytes yesterday')

writeData()

print('\n\n**************************\n\n')
os.system("tail -n 5 dataUsed.txt")

if tnow == str(lastDay):
    os.system(f"mv dataUsed.txt {endDate}.txt && touch dataUsed.txt")
