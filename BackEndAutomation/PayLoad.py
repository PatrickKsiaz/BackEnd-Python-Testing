from utilities.configurations import *

def addBookPayload(isbn):
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": "bcd",
        "aisle": "227",
        "author": "John Foe" 
    }
    return body


def getQuery():
    pass

def buildPayloadFromDB(query):

    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = ''
    addBody['aisle'] = ''
    addBody['author'] = ''
    return addBody

