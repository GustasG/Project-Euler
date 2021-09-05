from typing import List, Generic, TypeVar


T = TypeVar('T')


class CircularBuffer(Generic[T]):
    def __init__(self, values: List[T]) -> None:
        self.values = values

    def __getitem__(self, key: int) -> T:
        return self.values[key % len(self.values)]
