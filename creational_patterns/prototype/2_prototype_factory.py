import copy


class Address:
    def __init__(self, street_address, suite, city):
        self.street_address = street_address
        self.suite = suite
        self.city = city

    def __str__(self):
        return f'{self.street_address}, Suite: #{self.suite}, {self. city}'


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee_prototype = Employee('', Address('Legnicka 15', 0, 'Wroclaw'))
    aux_office_employee_prototype = Employee('', Address('Legnicka 17', 0, 'Wroclaw'))

    @staticmethod
    def __new_employee(proto, name, suite):
        employee = copy.deepcopy(proto)
        employee.name = name
        employee.address.suite = suite
        return employee

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.main_office_employee_prototype,
                                              name, suite)

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.aux_office_employee_prototype,
                                              name, suite)


if __name__ == '__main__':
    john = EmployeeFactory.new_main_office_employee('John', 12)
    jane = EmployeeFactory.new_aux_office_employee('Jane', 85)
    print(john)
    print(jane)
