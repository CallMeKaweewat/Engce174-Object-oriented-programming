#  การดำเนินการและเมธอดของชุดข้อมูล (Sets)

# ชุดข้อมูล (Sets)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

#  การเพิ่มองค์ประกอบลงในชุดข้อมูล
set1.add(5)

#  การลบองค์ประกอบออกจากชุดข้อมูล
set2.discard(6)

#  การตรวจสอบ subset และ superset
print("Is set1 a subset of set2?", set1.issubset(set2)) #  แสดงผล: Is set1 a subset of set2? False
print("Is set2 a superset of set1?", set2.issuperset(set1)) #  แสดงผล: Is set2 a superset of set1? True
