class Student:
    def __init__(self, code, name, average, sex, scholarship):
        self.code = code
        self.name = name
        self.average = average
        self.sex = sex
        self.scholarship = scholarship

    def __str__(self):
        return "code: {}, name: {}, sex: {}, average: {}".format(self.code, self.name, self.sex, self.average)
