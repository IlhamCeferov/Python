class Employee:

    total_employees = 0

    def __init__(self, first_name, last_name):
        Employee.total_employees = Employee.total_employees + 1
        self.employee_number = Employee.total_employees
        self.first_name = first_name
        self.last_name = last_name

    def print_information(self):
        print(f"{self.employee_number}: {self.first_name} {self.last_name}")

class HourlyPaid(Employee):

    def __init__(self, first_name, last_name, hourly_pay):
        self.hourly_pay = hourly_pay
        super().__init__(first_name, last_name)

    def print_information(self):
        super().print_information()
        print(f"Hourly pay: {self.hourly_pay}")

class MounthlyPaid(Employee):

    def __init__(self, first_name, last_name, mounthly_pay):
        self.mounthly_pay = mounthly_pay
        super().__init__(first_name, last_name)

    def print_information(self):
        super().print_information()
        print(f"Mounthly pay: {self.mounthly_pay}")

employees = []
employees.append(HourlyPaid("Ilham", "Jafarov", 15.95))
employees.append(MounthlyPaid("Jafar", "Jafarov", 3950))
employees.append(Employee("Hikmet", "Haciyev"))
employees.append(HourlyPaid("Elvin", "Jafarov", 16.35))

for e in employees:
    e.print_information()