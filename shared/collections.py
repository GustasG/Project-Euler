from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')


@dataclass(frozen=True)
class CircularBuffer(Generic[T]):
    values: list[T]

    def __getitem__(self, key: int) -> T:
        return self.values[key % len(self.values)]

    def __len__(self):
        return len(self.values)
