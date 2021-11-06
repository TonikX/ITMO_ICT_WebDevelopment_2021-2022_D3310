# Показать всех воинов и всех умнений

Выводит информацию обо всех войнах

**URL** : `/api/warriors_skill/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "profession": {
            "title": "Ranger",
            "description": "Powerful human"
        },
        "skill": [
            {
                "id": 1,
                "title": "Lightning bolt"
            }
        ],
        "race": "student",
        "name": "Tom",
        "level": 7
    }
]
```