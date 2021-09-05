from typing import List, Generic, TypeVar


T = TypeVar('T')


class CircularBuffer(Generic[T]):
    def __init__(self, values: List[T]) -> None:
        self.values = values

    def __getitem__(self, key: int) -> T:
        return self.values[key % len(self.values)]


def binary_search(collection: List[T], value: T) -> bool:
    first = 0
    last = len(collection) - 1

    while first <= last:
        mid = (first + last)//2

        if collection[mid] == value:
            return True
        else:
            if value < collection[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return False
