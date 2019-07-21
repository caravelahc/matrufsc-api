# matrufsc-api

Web server that exposes information gathered by [matrufsc-crawler](https://github.com/caravelahc/matrufsc-crawler/).

# Setup
This project uses `poetry` as the dependency manager. Install dependencies and run with:

```
poetry install
poetry run matrufsc-api -u ./db.json
```

Check available arguments and options with `poetry run matrufsc-crawler --help`.

# Endpoints

## `/courses`

Get data from all UFSC's courses.
- **GET**
- **Query**: _Optional:_ `semester` and `campus`

#### Example:

```
/courses?semester=20192&campus=FLO
---
[
  {
    "id": "ACL5111",
    "name": "Hematologia Clínica Veterinária",
    "class_hours": 36
  },
  {
    "id": "ACL5130",
    "name": "Biossegurança e Boas Práticas de Laboratório",
    "class_hours": 36
  },
]
```

## `/classes`
Detailed info about a specific class.

- **GET**
- **Query**: _Required:_ `semester` _Optional:_ `semester`

#### Example:
```
/classes?course_id=INE5403&semester=20192
---
[
  {
    "id": "01208A",
    "class_labels": [
      "Bloqueada (inativa)"
    ],
    "capacity": 25,
    "enrolled": 0,
    "special": 0,
    "waiting": null,
    "times": [
      "2.0820-2 / CTC-CTC303",
      "3.1010-2 / CTC-CTC302",
      "5.0730-2 / CTC-CTC105"
    ],
    "professors": [
      "Mauro Roisenberg"
    ]
  }
]
```

## `/semesters`
Returns the semesters that were crawled.

- **GET**

#### Example:
```
/semesters
---
[
  "20193",
  "20192"
]
```

## `/campi`
Returns the names from the available campi.

- **GET**

#### Example:
```
/campi
---
[
  "CBS",
  "JOI",
  "ARA",
  "BLN",
  "FLO"
]
```
