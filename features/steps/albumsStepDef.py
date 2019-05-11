import sys
sys.path.append('C:/Users/sbanchhor/Automation/Definiens')
from behave import *
from actions import automationMain

use_step_matcher("re")


@given('get "(.+)" for Method "(.+)"')
def step_impl(context, fetchUrl, apiMethod):
    """
    :type context: behave.runner.Context
    :type fetchUrl: str
    :type apiMethod: str
    """
    getApiUrl(fetchUrl)


@then('i verify api status code for api method "(.+)" of url "(.+)" is "(.+)" and response body matches json "(.+)" for json input "(.+)"')
def step_impl(context, apiMethod, fetchUrl, statusCode, jsonResponse, jsonInput):
    """
    :type context: behave.runner.Context
    :type apiMethod: str
    :type fetchUrl: str
    :type statusCode: str
    :type jsonResponse: str
    :type jsonInput: str
    """
    verifyApiResponse(apiMethod, fetchUrl, statusCode, jsonResponse,jsonInput)
