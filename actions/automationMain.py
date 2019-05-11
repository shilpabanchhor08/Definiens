import sys
import requests
import json

apiBaseUrl = "https://jsonplaceholder.typicode.com/"

def getApiUrl(apiFetchUrl):
    apiFinalUrl = apiBaseUrl + apiFetchUrl
    requests.get(apiFinalUrl)
    return


def getApiResponse(responseCode, apiFetchUrl):
    apiFinalUrl = apiBaseUrl + apiFetchUrl
    singleAlbumResponse = requests.get(apiFinalUrl)
    print(singleAlbumResponse.status_code)
    assert (str(singleAlbumResponse.status_code) == responseCode), "Response Not OK"
    print("GET API Response : OK")

