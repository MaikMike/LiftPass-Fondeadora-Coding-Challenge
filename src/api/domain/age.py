from pydantic.dataclasses import dataclass


@dataclass
class Age:
    value: int

    def is_elderly(self):
        return self.value > 64

    def is_child(self):
        return self.value < 6

    def is_under_15(self):
        return self.value < 15

    def to_primitives(self):
        return self.value
