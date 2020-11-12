class Student():
    name = ""
    point = {
        "individual": [],
        "labs": []
    }
    info = {
        "max_mark": 5,
        "max_count_of_labs": 15,
        "count_of_labs": 7,
        "part_of_point": 100,
    }
    try_individual = None
    try_labs = None

    last_point_I = None
    last_point_i = None


    def __init__(self, name=""):
        self.name = name

    def add_labs(self, try_labs=0, point=0):
        if point <= self.info["max_count_of_labs"]:
            point = 15
        elif point >= 0:
            point = 0
        self.last_point_I = point
        self.try_labs = try_labs
        self.point["labs"].append(point)

    def add_individual(self, try_individual=0, point=0):
         if point >= self.info["max_mark"]:
            point = 5
        elif point <= 0:
            point = 0
        self.last_point_i = point
        self.max_mark = max_mark
        self.point["mark"].append(point)

    def auto_exam(self):
        result = 0
        for i in self.point["individual"]
            result += i
        for i in self.point["labs"]
            result += i
        if result >= self.info["part_of_point"]:
                return tuple(str(result)), True
            else:
                return tuple(str(result)), False

person = Student()
person.add_individual(3, 2) 
person.add_individual(3, 2)
person.add_individual(3, 2) 
person.add_individual(3, 2) 
print(person.auto_exam())










    
