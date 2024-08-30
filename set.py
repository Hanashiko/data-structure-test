from typing import Set, Union

Set1: Set[Union[int, str]] = set([1, 2, 'Windows', 4, "Linux", 6, "Mac"])
print(f"Set with the use of Mixed Values: {Set1}")

print("Elements of set: ")
for i in Set1:
    print(i, end = " ")
print()

print("Linux" in Set1)