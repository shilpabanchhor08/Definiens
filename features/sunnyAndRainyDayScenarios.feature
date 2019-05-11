Feature: Verifying positive and negative scenarios
  Scenario Outline: Albums
    Given get Url "<fetch url>"
    Then i verify all album ID's must be unique for url "<fetch url>"
    And i verify all album Title must be unique for url "<fetch url>"
    And i verify invalid album id "<input id>" using url "<fetch url>"
    And i verify invalid album title "<input title>" using url "<fetch url>"
    Examples:
      | fetch url | input id | input title |
      | albums | 1001 | BSDK |

  Scenario Outline: users
    Given get Url "<fetch url>"
    Then i verify all user email ID's must be unique for url "<fetch url>"
    And i verify invalid user email id "<input id>" using url "<fetch url>"
    Examples:
      | fetch url | input id |
      | users | BSDK.com |



