Feature: General API Testing
  Scenario Outline:
    Given get "<fetch url>" for Method "<api method>"
    Then i verify api status code for api method "<api method>" of url "<fetch url>" is "<response code>" and response body matches json "<json response>" for json input "<json input>"
    Examples:
      | fetch url | api method | response code | json response | json input |
      | albums/1 | GET | 200 | {"userId": 1, "id": 1, "title": "quidem molestiae enim"} | {} |
      | albums/1 | DELETE | 200 | {}| {} |
      | albums/1 | PUT | 200 | {"userId": "1", "id": 1, "title": "shilpa1"} | {  "userId": 1,  "id": 1,  "title": "shilpa1"} |
      | albums | POST | 201 | {"userId": "1", "id": 101, "title": "shilpa"} | {"userId": 1,"id": 10,"title": "shilpa"} |



