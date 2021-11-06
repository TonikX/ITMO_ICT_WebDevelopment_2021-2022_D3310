# Показать список студентов

**URL** : `report/<int:pk>`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "Средний балл": {
        "score_math__avg": 60.333333333333336,
        "score_chemical__avg": 82.33333333333333,
        "score_english__avg": 42.0,
        "score_computer__avg": 70.33333333333333
    },
    "Обшие люди": {
        "last_name__count": 3
    },
    "руководитель": [
        {
            "id": 1,
            "head_teacher": "Jinping",
            "number": "D1000"
        }
    ]
}
```