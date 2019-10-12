import json
import sys


def readLog(filename):
    fp = open(filename)

    eventLog = []

    for line in fp:
        event = json.loads(line)
        if event["detectedDuplicate"] == False and event["detectedCorruption"] == False:
            eventLog.append(event)

    return eventLog


def userAgents(eventLog):

    listUserAgents = set()

    for line in eventLog:
        listUserAgents.add(line["userAgentName"])

    return len(listUserAgents)


if __name__ == '__main__':

    eventLog = readLog(sys.argv[1])

    valUserAgents = userAgents(eventLog)
    print("Число различных браузеров среди всех клиентов: {}".format(valUserAgents))
