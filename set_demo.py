nums = {10, 20, 30, 4, 22, 5, 6, 33}
nums2 = {10, 4, 6, 44, 55}
print(nums)
print(nums2)

print(11 in nums)

print(nums | nums2)
print(nums & nums2)  # Intersection
print(nums ^ nums2)  # XOR

chars = set("Python Programming")
print(chars)

langs = set()

langs.add("Java")
langs.add("Python")

print(langs.isdisjoint({"c#", "C"}))
