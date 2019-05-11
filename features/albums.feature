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
      | albums?userId=2 | FILTER | 200 | [{"userId": 2, "id": 11, "title": "quam nostrum impedit mollitia quod et dolor"}, {"userId": 2, "id": 12, "title": "consequatur autem doloribus natus consectetur"}, {"userId": 2, "id": 13, "title": "ab rerum non rerum consequatur ut ea unde"}, {"userId": 2, "id": 14, "title": "ducimus molestias eos animi atque nihil"}, {"userId": 2, "id": 15, "title": "ut pariatur rerum ipsum natus repellendus praesentium"}, {"userId": 2, "id": 16, "title": "voluptatem aut maxime inventore autem magnam atque repellat"}, {"userId": 2, "id": 17, "title": "aut minima voluptatem ut velit"}, {"userId": 2, "id": 18, "title": "nesciunt quia et doloremque"}, {"userId": 2, "id": 19, "title": "velit pariatur quaerat similique libero omnis quia"}, {"userId": 2, "id": 20, "title": "voluptas rerum iure ut enim"}] | {} |
      | users/1/albums?id=2 | NESTED | 200 | [{"userId": 1, "id": 2, "title": "sunt qui excepturi placeat culpa"}] | {} |


