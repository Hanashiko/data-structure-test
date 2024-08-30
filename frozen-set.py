from typing import Set, FrozenSet

normal_set: Set[str] = set(["a", "b", "c", "d"])
print(f"Normal Set: {normal_set}")

frozen_set: FrozenSet[str] = frozenset(["a", "s", "d", "f"])
print(f"Frozen Set: {frozen_set}")