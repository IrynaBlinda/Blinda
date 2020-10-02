from dataclasses import dataclass


@dataclass
class DepartmentStoreTurnover:
    code: int
    plan: int
    implementation: int
    year: int


@dataclass
class DirectoryOfProductGroups:
    code: int
    name: str
    sale: float


department_array = []
department_array.append(DepartmentStoreTurnover(1000, 4340, 4420, 2013))
department_array.append(DepartmentStoreTurnover(2000, 6280, 6720, 2013))
department_array.append(DepartmentStoreTurnover(3000, 5260, 5854, 2013))
department_array.append(DepartmentStoreTurnover(4000, 3720, 3682, 2013))
department_array.append(DepartmentStoreTurnover(5000, 2410, 2694, 2013))
department_array.append(DepartmentStoreTurnover(1000, 4600, 4640, 2014))
department_array.append(DepartmentStoreTurnover(2000, 6800, 7400, 2014))
department_array.append(DepartmentStoreTurnover(3000, 6000, 6250, 2014))
department_array.append(DepartmentStoreTurnover(4000, 3800, 3850, 2014))
department_array.append(DepartmentStoreTurnover(5000, 2700, 3000, 2014))
department_array.append(DepartmentStoreTurnover(1000, 4700, 4625, 2015))
department_array.append(DepartmentStoreTurnover(2000, 6700, 6630, 2015))
department_array.append(DepartmentStoreTurnover(3000, 6700, 6500, 2015))
department_array.append(DepartmentStoreTurnover(4000, 4300, 4500, 2015))
department_array.append(DepartmentStoreTurnover(5000, 3500, 3590, 2015))

product_array = []
product_array.append(DirectoryOfProductGroups(1000, "Тканини", 4))
product_array.append(DirectoryOfProductGroups(2000, "Одяг та білизна", 7.5))
product_array.append(DirectoryOfProductGroups(3000, "Взуття", 7.5))
product_array.append(DirectoryOfProductGroups(4000, "Трикотаж", 7.5))
product_array.append(DirectoryOfProductGroups(5000, "Галантерея", 9.5))


def printDepartmentStoreTurnover(departmentStoreTurnover):
    '''printDepartmentStoreTurnover function prints
       "Товарообіг універмагу"
        with names and values'''

    print("Код: {code}, План: {plan}, Очікуєме виконання: {implementation}, Рік: {year}"
          .format(code=departmentStoreTurnover.code, plan=departmentStoreTurnover.plan, implementation=departmentStoreTurnover.implementation,
                  year=departmentStoreTurnover.year))


for data in department_array:
    printDepartmentStoreTurnover(data)


def printDirectoryOfProductGroups(directoryOfProductGroups):
    '''printDirectoryOfProductGroups function prints
       "Довідник товарних груп"
       with names and values'''

    print("Код товарної групи: {code}, Найменування товарної групи: {name}, Торгова скидка, %: {sale}"
          .format(code=directoryOfProductGroups.code, name=directoryOfProductGroups.name, sale=directoryOfProductGroups.sale))


for data in product_array:
    printDirectoryOfProductGroups(data)
