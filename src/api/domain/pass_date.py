from pydantic.dataclasses import dataclass
from datetime import date


@dataclass
class PassDate:
    value: date

    def is_monday_pass(self):
        MONDAY_ISO_DAY = 0
        return self.value.weekday() == MONDAY_ISO_DAY

    def to_primitives(self):
        return self.value
