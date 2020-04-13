import datetime
"""
This code gets the start and stop dates for my usage period.

It will also remove the start and stop dates once the period as ended.
"""


def getdates():
    with open('dates.txt', 'r+') as f:
        lineList = f.readline().split(",")
        start = datetime.date.fromisoformat(lineList[0])
        stop = datetime.date.fromisoformat(lineList[1])
        lastDay = stop + datetime.timedelta(days=1)
        tnow = datetime.date.today()
        if tnow >= lastDay:
            line = ",".join(lineList[2:])
            f.seek(0)
            f.write(line)
        return start, stop
