import sys
import requests
import json

apiBaseUrl = "https://jsonplaceholder.typicode.com/"


def getApiUrl(fetchUrl):
    apiFinalUrl = apiBaseUrl + fetchUrl
    requests.get(apiFinalUrl)
    return

def verifyAlbumIdValueIsUnique(fetchUrl):
    apiFinalUrl = apiBaseUrl + fetchUrl
    jsonResponse=requests.get(apiFinalUrl).json()
    jsonResponseLength = len(jsonResponse)
    mySet = set()
    for k in range(0,len(jsonResponse)):
        dict=(list(jsonResponse[k].values()).__getitem__(1))
        mySet.add(dict)
    lengthOfSet = len(mySet)
    assert (jsonResponseLength == lengthOfSet), "JSON Values are Duplicate \n"
    print("All the Values are Unique \n")


def verifyAlbumTitleIsUnique(fetchUrl):
    apiFinalUrl = apiBaseUrl + fetchUrl
    jsonResponse=requests.get(apiFinalUrl).json()
    jsonResponseLength = len(jsonResponse)
    mySet = set()
    for k in range(0,len(jsonResponse)):
        dict=(list(jsonResponse[k].values()).__getitem__(2))
        mySet.add(dict)
    lengthOfSet = len(mySet)
    assert (jsonResponseLength == lengthOfSet) , "JSON Titles are Duplicate \n"
    print("All the Titles are Unique \n")

def verifyEmailIdIsUnique(fetchUrl):
    apiFinalUrl = apiBaseUrl + fetchUrl
    jsonResponse=requests.get(apiFinalUrl).json()
    jsonResponseLength = len(jsonResponse)
    mySet = set()
    for k in range(0,len(jsonResponse)):
        dict=(list(jsonResponse[k].values()).__getitem__(3))
        mySet.add(dict)
    lengthOfSet = len(mySet)
    assert (jsonResponseLength == lengthOfSet), "JSON E-mailid is Duplicate \n"
    print("All the E-mailid is Unique \n")


def verifyInvalidAlbumId(fetchUrl,input):
    apiFinalUrl = apiBaseUrl + fetchUrl
    jsonResponse=requests.get(apiFinalUrl).json()
    jsonResponseLength = len(jsonResponse)
    mySet = set()
    flag= False
    for k in range(0,len(jsonResponse)):
        dict=(list(jsonResponse[k].values()).__getitem__(1))
        if dict==input:
            flag = True

    assert (flag == False), "ID Exists"
    print("Assertiion Validated, ID Does Not Exist \n")

def verifyInvalidEmailRecord(fetchUrl,input):
    apiFinalUrl = apiBaseUrl + fetchUrl
    jsonResponse=requests.get(apiFinalUrl).json()
    jsonResponseLength = len(jsonResponse)
    mySet = set()
    flag= False
    for k in range(0,len(jsonResponse)):
        dict=(list(jsonResponse[k].values()).__getitem__(3))
        if dict==input:
            flag = True

    assert (flag == False), "EmailID Exists"
    print("Assertiion Validated, EmailID Does Not Exist \n")

def verifyInvalidTitleRecord(fetchUrl,input):
    apiFinalUrl = apiBaseUrl + fetchUrl
    jsonResponse=requests.get(apiFinalUrl).json()
    jsonResponseLength = len(jsonResponse)
    mySet = set()
    flag= False
    for k in range(0,len(jsonResponse)):
        dict=(list(jsonResponse[k].values()).__getitem__(2))
        if dict==input:
            flag = True

    assert (flag == False), "Title Exists"
    print("Assertiion Validated, Title Does Not Exist \n")





# verifyInvalidRecord(apiFinalUrl)
# verifyInvalidEmailRecord(apiFinalUrl)
# verifyInvalidTitleRecord(apiBaseUrl)


