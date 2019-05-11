import sys
import requests
import json

apiBaseUrl = "https://jsonplaceholder.typicode.com/"

def getApiUrl(apiFetchUrl):
    apiFinalUrl = apiBaseUrl + apiFetchUrl
    requests.get(apiFinalUrl)
    return


def verifyApiResponse(apiMethodValue, fetchUrl, statusCode, jsonResponse,jsonInput):
    apiFinalUrl = apiBaseUrl + fetchUrl
    apiCallInput = json.loads(jsonInput)
    apiResponse = apiMethod(apiMethodValue,apiFinalUrl,apiCallInput)
    assert (str(apiResponse.status_code) == statusCode), "Response Not OK"
    print(apiMethodValue + " API status code Response : OK ")
    assert (json.dumps(apiResponse.json())==jsonResponse),"Response Not OK"
    print(apiMethodValue + " API json Response  : OK \n")

def apiMethod(restApiMethod,apiFinalUrl,jsonInput ):
    switcher={
        "GET": requests.get(apiFinalUrl),
        "POST": requests.post(apiFinalUrl,data=jsonInput),
        "PUT": requests.put(apiFinalUrl,data=jsonInput),
        "DELETE": requests.delete(apiFinalUrl),
        "FILTER": requests.get(apiFinalUrl),
        "NESTED": requests.get(apiFinalUrl)
    }
    return switcher.get(restApiMethod, "Invalid Rest API Method Passed")

