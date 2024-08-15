# Example 2: Set operations  (Sets)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Union of two setd  (Union)
union_set = set1 | set2
print("Union set:", union_set) # Output: Union set: {1, 2, 3, 4, 5, 6, 7} 

# Intersection of two sets  (Intersection)
intersection_set = set1 & set2
print("Intersection set:", intersection_set) # Output: Intersection set: {3, 4, 5} 

# Difference between two sets  (Difference)
difference_set = set1 - set2
print("Difference set (set1 - set2):", difference_set) # Output: Difference set (set1 - set2): {1, 2} 

# Symmetric difference between two sets  (Symmetric Difference)
symmetric_difference_set = set1 ^ set2
print("Symmetric difference set:", symmetric_difference_set) # Output: Symmetric difference set: {1, 2, 6, 7} 