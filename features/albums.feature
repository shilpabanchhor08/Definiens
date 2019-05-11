Feature: General API Testing
  Scenario Outline:
    Given get "<fetch url>" with expected data in file propFile
    Then i verify api status code is "<response code>" and response body is not null from "<fetch url>"
    Examples:
      | fetch url | response code |
      | albums/1  |  200 |

