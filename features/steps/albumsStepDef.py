from behave import *

from actions.automationMain import getApiResponse, getApiUrl

use_step_matcher("re")

@given('get "(.+)" with expected data in file propFile')
def step_fetchUrl(context, fetchUrl):
    """
    :type context: behave.runner.Context
    :type fetchUrl: str
    :type propFile: str
    """

    getApiUrl(fetchUrl)


@then('i verify api status code is "(.+)" and response body is not null from "(.+)"')
def step_impl(context, responseCode, fetchURL):
    """
    :type context: behave.runner.Context
    :type arg0: str
    :type arg1: str
    """
    getApiResponse(responseCode, fetchURL)