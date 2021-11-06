# Показать одно расписание

**URL** : `schedules/<int:pk>`

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
    "classroom": "1000",
    "teacher": "Jinping",
    "time": "06:00:00",
    "day": "mon",
    "subject": "m"
}
```