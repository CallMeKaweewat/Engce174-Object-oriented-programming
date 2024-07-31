#  การทำงานกับดิกชันนารี

#  สร้างดิกชันนารีของเกรดนักเรียน
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 88, 'David': 95}

#  เข้าถึงค่าโดยใช้คีย์
print("Bob's grade:", grades['Bob']) # Output: Bob's grade: 92 แสดงผล: Bob's grade: 92

#  เพิ่มข้อมูลใหม่
grades['Eve'] = 90

#  การวนลูปผ่านคีย์และค่า
for student, grade in grades.items():
    print(f"{student}: {grade}")
    
#  ใช้เมธอด get() เพื่อลดโอกาสการเกิด KeyError
print("Frank's garde:", grades.get('Frank','Grade not found')) #  แสดงผล: Frank's grade: Grade not found
