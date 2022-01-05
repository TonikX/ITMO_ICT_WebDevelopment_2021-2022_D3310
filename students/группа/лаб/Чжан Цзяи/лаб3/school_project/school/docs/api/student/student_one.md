# Показать одного студента

**URL** : `students/<int:pk>`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "group": "D1000",
    "sex": "m",
    "first_name": "Jiayi",
    "last_name": "Jiang",
    "score_math": 60,
    "score_chemical": 80,
    "score_english": 20,
    "score_computer": 100,
    "semester": 1
}
```