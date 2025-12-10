from typing import Any

score = [7.8, 8.0, 6.5, 9.0, 8.5]

def get_min_max(num: list[float]) -> tuple[float, float]:
    minium = min(num)
    maximum = max(num)
    return maximum, minium

def get_total(numbs: list[float]) -> float:
    total = sum(numbs) / len(numbs)
    return total

max_score, min_score = get_min_max(score)
total = get_total(score)
print("Tong diem:", total)
print("Diem cao nhat", max_score)
print("Diem thap nhat", min_score )


nums = [5, -2, 8, -1, 0, 3, -10]

def remove_negative_numbers(nums: list[float]) -> list[float]:
    evens = [x for x in nums if x>=0]
    return evens

print(remove_negative_numbers(nums))

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = [7, 8, 9]

for i in range(len(arr1)):
    arr2.append(arr1[i])
    arr2.append(arr3[i])

print(sorted(arr2))

#==================Dictionary=============================

student: dict[str, Any] = {
    "name": "Nguyen Van A",
    "age": 20,
    "scores": [7.5, 8.0, 6.5, 9.0],
}
keys = list(student.keys())

print(keys[0],":",student.get("name"))
print()