from pydantic.dataclasses import dataclass


@dataclass
class PassType:
    value: str

    def is_night_pass(self):
        return self.value == 'Night'

    def is_day_pass(self):
        return self.value == 'Jour'

    def to_primitives(self):
        return self.value
