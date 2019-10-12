import json
import sys
import collections


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

def itemsFavorites(eventLog):

    listItems = set()

    for line in eventLog:
        if line["eventType"] == "itemFavEvent":
            listItems.add(line["item_id"])  

    return len(listItems)

def itemsLike(eventLog):

    counter = collections.Counter()
    
    for line in eventLog:
        if line["eventType"] == "itemFavEvent":
            counter[line["item_id"]] += 1

    return counter

if __name__ == '__main__':

    eventLog = readLog(sys.argv[1])

    valUserAgents = userAgents(eventLog)
    print("Число различных браузеров среди всех клиентов: {}".format(valUserAgents))

    sumPrice = itemPrice(eventLog)
    print("Сумма всех покупок: {}".format(sumPrice))

    valItemFavorites = itemsFavorites(eventLog)
    print("Число различных товаров, которые были добавлены в избранное: {}".format(valItemFavorites))

    counter = itemsLike(eventLog)
    for item, cnt in counter.most_common(10):
        print("Популярные товары {} -- {}".format(item, cnt))

    counter = itemsLike(eventLog)
    for item, cnt in counter.most_common()[:-2:-1]:
        print("Самый непопулярный товар {} -- {}".format(item, cnt))