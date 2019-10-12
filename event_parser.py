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

def itemPrice(eventLog):

    sum = 0

    for line in eventLog:
        if line["eventType"] == "itemBuyEvent":
            sum += int(line["item_price"])

    return sum


if __name__ == '__main__':

    eventLog = readLog(sys.argv[1])

    valUserAgents = userAgents(eventLog)
    print("Число различных браузеров среди всех клиентов: {}".format(valUserAgents))

    sumPrice = itemPrice(eventLog)
    print("Сумма всех покупок: {}".format(sumPrice))
