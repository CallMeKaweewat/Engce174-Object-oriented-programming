class Employee:
    def __init__(self, name, salary): # กำหนดชื่อและเงินเดือนของพนักงาน
        self.name = name 
        self.salary = salary 

    def annual_salary(self): # ฟังก์ชันคำนวณเงินเดือนรายปี
        return self.salary * 12 

class Manager(Employee): # คลาส Manager สืบทอดคุณสมบัติและพฤติกรรมจากคลาส Employee
    def __init__(self, name, salary, bonus): 
        super().__init__(name, salary) 
        self.bonus = bonus 

    def annual_salary(self): # ฟังก์ชันคำนวณเงินเดือนรายปีรวมกับโบนัส
        return (self.salary * 12) + self.bonus 

class Developer(Employee): # คลาส Developer สืบทอดคุณสมบัติและพฤติกรรมจากคลาส Employee
    def __init__(self, name, salary, projects): 
        super().__init__(name, salary) 
        self.projects = projects 

    def annual_salary(self): # ฟังก์ชันคำนวณเงินเดือนรายปีรวมกับค่าตอบแทนจากโครงการ
        base_salary = self.salary * 12 
        return base_salary + (self.projects * 1000) 

# สร้างออบเจ็กต์ manager ของคลาส Manager โดยกำหนดชื่อเป็น "Alice", เงินเดือน 6000 หน่วย, และโบนัส 5000 หน่วย
manager = Manager("Alice", 6000, 5000) 

# สร้างออบเจ็กต์ developer ของคลาส Developer โดยกำหนดชื่อเป็น "Bob", เงินเดือน 5000 หน่วย, และจำนวนโครงการ 3 โครงการ
developer = Developer("Bob", 5000, 3) 

# คำนวณเงินเดือนรายปีรวมของผู้จัดการและนักพัฒนา
total_annual_salary = manager.annual_salary() + developer.annual_salary() 

# แสดงผลรวมเงินเดือนรายปีของผู้จัดการและนักพัฒนา
print(total_annual_salary)