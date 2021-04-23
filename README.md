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

### Setup database

```
touch test.db
pipenv run python setup
```

### Server

Install dependencies

```
pipenv install
```

Set variables

```
pipenv shell
export FLASK_APP=src/app.py
```

Run project

```
flask run
```

### Tests

```shell
pytest src/test/test_day_pass_prices_calculator.py
pytest src/test/test_night_pass_prices_calculator.py

```
