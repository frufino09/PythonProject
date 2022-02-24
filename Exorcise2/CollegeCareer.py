from Student import Student


class CollegeCareer:
    def __init__(self):
        self.students_list = [
            Student("II2114", "Juanito", 9.56, "Masculine", True),
            Student("BC7865", "Andrea", 6.70, "Feminine", False),
            Student("HG4112", "Pablo", 8.50, "Masculine", False),
            Student("PO8782", "Alejandra", 5.20, "Feminine", True)
        ]

    def number_of_scholarship_holders(self):
        scholarship_count = 0
        for student in self.students_list:
            if student.scholarship:
                scholarship_count += 1
        return scholarship_count

    def list_of_students_in_a_given_group(self, group_number):
        group_student_list = []
        for student in self.students_list:
            if group_number in student.code:
                group_student_list.append(student)
        return group_student_list

    def student_visualization(self, code_student):
        for student in self.students_list:
            if code_student == student.code:
                return student
        return None

    def female_average_list(self):
        list_female = []
        for student in self.students_list:
            if student.sex == "Feminine":
                list_female.append(student.average)
        return list_female[::-1]

    def total_male_group(self, group_number):
        count_male = 0
        for student in self.students_list:
            if group_number in student.code and student.sex == "Masculine":
                count_male += 1
        return count_male

    @staticmethod
    def method():
        return 5 + 6
