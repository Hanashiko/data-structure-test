from typing import Tuple, List

Tuple1: Tuple[str] = ("Windows", "Linux")
print(f"Tuple with the use of String: {Tuple1}")

list1: List[int] = [1, 2, 3, 4, 5, 6]
print("Tuple using List: ", end="")
Tuple1: Tuple[int] = tuple(list1)
print(Tuple1)

print(f"First element of tuple: {Tuple1[0] = }")
print(f"Last element of tuple: {Tuple1[-1] = }")
print(f"Third last element of tuple: {Tuple1[-3] = }")