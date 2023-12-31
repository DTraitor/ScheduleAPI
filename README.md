# Schedule API
This is an API for schedule management in a university. It is written in Python using Django framework.

# Entities

## Group
| Field      |  Type   | Nullable | Description                            |
|:-----------|:-------:|:--------:|:---------------------------------------|
| id         | String  |    No    | UUID of the group                      |
| name       | String  |    No    | Full name of the group (e.g. FCSE 521) |
| short_name | String  |    No    | Short name of the group (e.g. SE-121M) |

## Lesson
| Field       |  Type   | Nullable | Description                           |
|:------------|:-------:|:--------:|:--------------------------------------|
| id          | String  |    No    | UUID of the lesson                    |
| name        | String  |    No    | Name of the lesson (e.g. Programming) |
| short_name  | String  |    No    | Short name of the lesson (e.g. Prog)  |
| description | String  |    No    | Description of the lesson             |
| teacher     | String  |    No    | Name of the teacher                   |
| link        | String  |    No    | Link to google meet or similar        |
| location    | String  |    No    | Room where the lesson is held         |
| kind        | Integer |    No    | Type of the lesson ()                 |
TODO: add kind
# Endpoints
| Link                | HTTP Method | Description                           |            Params             |
|:--------------------|:-----------:|:--------------------------------------|:-----------------------------:|
| /api/create_group/  |    POST     | Creates a new group                   | [\*click*](#apicreate_group)  |
| /api/delete_group/  |     DEL     | Deletes the group                     | [\*click*](#apidelete_group)  |
| /api/find_groups/   |     GET     | Searches for groups with similar name |  [\*click*](#apifind_groups)  |
| /api/get_group/     |     GET     | Returns a group by id                 |   [\*click*](#apiget_group)   |
| /api/add_lesson/    |    POST     | Add a lesson to the group             |  [\*click*](#apiadd_lesson)   |
| /api/delete_lesson/ |     DEL     | Delete planned lesson                 | [\*click*](#apidelete_lesson) |
| /api/get_lessons/   |     GET     | Get lessons on a date                 |  [\*click*](#apiget_lessons)  |

### /api/create_group/
#### Query params
| Field      |  Type   | Nullable | Description                            |
|:-----------|:-------:|:--------:|:---------------------------------------|
| name       | String  |    No    | Full name of the group (e.g. FCSE 521) |
| short_name | String  |    No    | Short name of the group (e.g. SE-121M) |
#### Return
| Field      |  Type   | Nullable | Description                            |
|:-----------|:-------:|:--------:|:---------------------------------------|
| id         | String  |    No    | UUID of the group                      |
| name       | String  |    No    | Full name of the group (e.g. FCSE 521) |
| short_name | String  |    No    | Short name of the group (e.g. SE-121M) |

### /api/delete_group/
#### Query params
| Field |  Type  | Nullable | Description       |
|:------|:------:|:--------:|:------------------|
| id    | String |    No    | UUID of the group |
#### Return
| Field   |  Type  | Nullable | Description     |
|:--------|:------:|:--------:|:----------------|
| message | String |    No    | Success message |

### /api/find_groups/
#### Query params
| Field |  Type  | Nullable | Description                             |
|:------|:------:|:--------:|:----------------------------------------|
| name  | String |    No    | Part of the full or short name of group |
#### Return
| Field  |       Type        | Nullable | Description                            |
|:-------|:-----------------:|:--------:|:---------------------------------------|
| groups | [[Group](#group)] |    No    | Array of groups that match the request |

### /api/get_group/
#### Query params
| Field |  Type  | Nullable | Description       |
|:------|:------:|:--------:|:------------------|
| id    | String |    No    | UUID of the group |
#### Return
| Field      |  Type   | Nullable | Description                            |
|:-----------|:-------:|:--------:|:---------------------------------------|
| id         | String  |    No    | UUID of the group                      |
| name       | String  |    No    | Full name of the group (e.g. FCSE 521) |
| short_name | String  |    No    | Short name of the group (e.g. SE-121M) |

### /api/add_lesson/
#### Query params
| Field           |  Type   | Nullable | Description                                                                                    |
|:----------------|:-------:|:--------:|:-----------------------------------------------------------------------------------------------|
| group_id        | String  |    No    | UUID of the group that the lesson belongs to                                                   |
| name            | String  |    No    | Name of the lesson (e.g. Programming)                                                          |
| short_name      | String  |    No    | Short name of the lesson (e.g. Prog)                                                           |
| description     | String  |    No    | Description of the lesson                                                                      |
| teacher         | String  |    No    | Name of the teacher                                                                            |
| link            | String  |    No    | Link to Google Meet or similar                                                                 |
| location        | String  |    No    | Room where the lesson is held                                                                  |
| kind            | Integer |    No    | Lesson type Lesson type (0 - lecture, 1 - practice, 2 - lab, 3 - seminar, 4 - exam, 5 - other) |
| time_start      | String  |    No    | Date when the lesson starts                                                                    |
| time_end        | String  |    No    | Date when the lesson ends                                                                      |
| repeat_type     | Integer |    No    | How often to repeat (0 - yearly, 1 - monthly, 2 - weekly, 3 - daily)                           |
| repeat_interval | Integer |    No    | Interval between repeats                                                                       |

#### Return
| Field      |       Type        | Nullable | Description                  |
|:-----------|:-----------------:|:--------:|:-----------------------------|
| group      |  [Group](#group)  |    No    | Group assigned to the lesson |
| lesson     | [Lesson](#lesson) |    No    | Lesson object                |

### /api/delete_lesson/
#### Query params
| Field |  Type  | Nullable | Description       |
|:------|:------:|:--------:|:------------------|
| id    | String |    No    | UUID of the group |
#### Return
| Field |      Type       | Nullable | Description                  |
|:------|:---------------:|:--------:|:-----------------------------|
| group | [Group](#group) |    No    | Group assigned to the lesson |

### /api/get_lessons/
#### Query params
| Field    |  Type  | Nullable | Description       |
|:---------|:------:|:--------:|:------------------|
| group_id | String |    No    | UUID of the group |
| date     | String |    No    | ISO date          |
#### Return
| Field   |        Type         | Nullable | Description                             |
|:--------|:-------------------:|:--------:|:----------------------------------------|
| group   |  [Group](#group)    |    No    | Group assigned to the lesson            |
| lessons | [[Lesson](#lesson)] |    No    | Array of lessons that match the request |
| count   |       Integer       |    No    | Number of lessons                       |