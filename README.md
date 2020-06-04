# Lift Pass

This application solves the problem of calculating the pricing for ski lift passes.

## Pricing

- Day passes:
  - Passes are free for people younger than 6.
  - Mondays have a 35% discount if it’s not a holiday.
  - People younger than 15 only pay 70% of the tariff but Monday discount does not apply.
  - People older than 64 only pay 75% of the tariff.
- Night passes:
  - Passes are free for people younger than 6.
  - People older than 64 only pay a 40% of the tariff.

## Challenge

The code is difficult to unit test or extend due to bad design. The business logic is tied to the framework and SQL.

## Running

### Server

```
FLASK_APP=src/app.py flask run
```

### Tests

```shell
pytest test_app.py
```
