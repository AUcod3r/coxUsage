import datetime


def getdates():
    with open('dates.txt', 'r+') as f:
        lineList = f.readline().split(",")
        start = lineList[0].split("-")
        start = datetime.date(int(start[0]), int(start[1]), int(start[2]))
        stop = lineList[1].split("-")
        stop = datetime.date(int(stop[0]), int(stop[1]), int(stop[2]))
        lastDay = stop + datetime.timedelta(days=1)
        if datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d") == str(lastDay):
            line = ",".join(lineList[2:])
            f.seek(0)
            f.write(line)
        return start, stop
