from typing import List

List1: List[str] = ["Windows", "Linux", "Mac"]
print(f"List containing multiple values: {List1}")

List2: List[list[str]] = [["Windows", "Mac"],["Linux"]]
print(f"Multi-Dimensional List: {List2}")

print("Accessing element from the list: ")
print(f"{List1[0] = }")
print(f"{List1[2] = }")

print("Accessing element using negative indexing")
print(f"{List1[-1] = }")
print(f"{List1[-3] = }")
