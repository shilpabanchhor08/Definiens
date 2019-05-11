from behave import *

from actions.positiveAndNegativeScenarios import verifyAlbumIdValueIsUnique, verifyAlbumTitleIsUnique, verifyEmailIdIsUnique, getApiUrl,\
    verifyInvalidEmailRecord, verifyInvalidTitleRecord ,verifyInvalidAlbumId

use_step_matcher("re")

@given('get Url "(.+)"')
def step_impl(context, fetchUrl):
    """
    :type context: behave.runner.Context
    :type fetchUrl: str
    """
    getApiUrl(fetchUrl)

@then('i verify all album ID\'s must be unique for url "(.+)"')
def stepVerifyid(context, fetchUrl):
    """
    :type context: behave.runner.Context
    :type fetchUrl: str
    """
    verifyAlbumIdValueIsUnique(fetchUrl)


@step('i verify all album Title must be unique for url "(.+)"')
def stepVerifyTitle(context, fetchUrl):
    """
    :type context: behave.runner.Context
    :type fetchUrl: str
    """
    verifyAlbumTitleIsUnique(fetchUrl)


@step('i verify all emailId must be unique for url "(.+)"')
def stepVerifyEmail(context, fetchUrl):
    """
    :type context: behave.runner.Context
    :type fetchUrl: str
    """
    verifyEmailIdIsUnique(fetchUrl)


@step('i verify invalid album id "(.+)" using url "(.+)"')
def stepInvalidId(context, fetchUrl, input):
    """
    :type context: behave.runner.Context
    :type fetchUrl: str
    :type input: str
    """
    verifyInvalidAlbumId(fetchUrl, input)



@step('i verify invalid album title "(.+)" using url "(.+)"')
def stepInvalidTitle(context, fetchUrl, input):
    """
    :type context: behave.runner.Context
    :type fetchUrl: str
    :type input: str
    """
    verifyInvalidTitleRecord(fetchUrl, input)

@then('i verify all user email ID\'s must be unique for url "(.+)"')
def step_UniqueEmail(context, fetchUrl):
    """
    :type context: behave.runner.Context
    :type fetchUrl: str
    """
    verifyEmailIdIsUnique(fetchUrl)


@step('i verify invalid user email id "(.+)" using url "(.+)"')
def step_InvalidEmail(context, fetchUrl, input):
    """
    :type context: behave.runner.Context
    :type fetchUrl: str
    :type input: str
    """
    verifyInvalidEmailRecord(fetchUrl, input)
