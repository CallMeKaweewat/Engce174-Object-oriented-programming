#  (Sets)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

#  (Union)
union_set = set1 | set2
print("Union:", union_set) # result: Union: {1, 2, 3, 4, 5, 6}

#  (Intersection)
intersection_set = set1 & set2
print("Intersection:", intersection_set) # result: Intersection: {3, 4}

#  (Difference)
difference_set = set1 - set2
print("Difference:", difference_set) # result: Difference: {1, 2}

#  (Symmetric Difference)
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference:", symmetric_difference_set) # result: Symmetric Difference: {1, 2, 5, 6}