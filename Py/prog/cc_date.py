import datetime


def validate(dt):
    if dt < datetime.datetime.utcnow():
        print("cc expired")
    else:
        print("cc not expired")

validate(
    datetime.datetime.combine(
        datetime.date(2025, 1, 1),
        datetime.time(12, 45)
    )
)

validate(
    datetime.datetime.combine(
        datetime.date(2015, 1, 1),
        datetime.time(12, 45)
    )
)