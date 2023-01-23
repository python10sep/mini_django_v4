class Employee:
    company = "accenture"

    def __init__(self, name, designation, salary):
        self.name = name
        self._designation = designation
        self.__salary = salary

    # GETTER  ( CONVENTION )
    def get_designation(self):
        return self._designation

    # SETTER ( CONVENTION )
    def set_designation(self, new_designation):
        self._designation = new_designation

    @property
    def salary(self):  # GETTER
        return self.__salary

    @salary.setter  # SETTER
    def salary(self, new_value):
        self.__salary = new_value

    @property
    def compensation(self):  # GETTER
        return str(self.__salary / 78) + " USD"

    @compensation.setter
    def compensation(self, new_value):
        self.__salary = new_value


emp1 = Employee("Sujit", "Executive Director", 9000000)

emp1.compensation = 80  # SET
print(emp1.compensation)
print(emp1.salary)
