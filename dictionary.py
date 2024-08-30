from typing import Dict, Union, List

Dict1: Dict[Union[str, int], Union[str, List[int]]] = {"Name": "Linux", 4: [1, 2, 3, 4]}
print(f"Creating Dictionary: {Dict1}")

print(f"Accessing a element using key: \n\
{Dict1["Name"] = }\n\
{Dict1[4] = }")

print(f"Accessing a element using get: \n\
{Dict1.get(4) = }\n\
{Dict1.get("Name") = }")

myDict: Dict[int, int] = {x: x**2 for x in [1,2,3,4,5,6]}
print(myDict)
myDict2: Dict[int, int] = {x: x**2 for x in [i for i in range(1,10)]}
print(myDict2)
