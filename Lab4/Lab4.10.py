#  การดำเนินการกับชุดข้อมูล (Sets)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

#  การรวมชุดข้อมูล (Union)
union_set = set1 | set2
print("Union set:", union_set) #  แสดงผล: Union set: {1, 2, 3, 4, 5, 6, 7}

#  การตัดกันของชุดข้อมูล (Intersection)
intersection_set = set1 & set2
print("Intersection set:", intersection_set) #  แสดงผล: Intersection set: {3, 4, 5}

#  ความแตกต่างระหว่างชุดข้อมูล (Difference)
difference_set = set1 - set2
print("Difference set (set1 - set2):", difference_set) #  แสดงผล: Difference set (set1 - set2): {1, 2}

#  ความแตกต่างแบบสมมาตร (Symmetric Difference)
symmetric_difference_set = set1 ^ set2
print("Symmetric difference set:", symmetric_difference_set) #  แสดงผล: Symmetric difference set: {1, 2, 6, 7}
