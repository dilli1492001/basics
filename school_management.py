class student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grade={}
class course:
    def __init__(self,course_name,course_code):
        self.course_name=course_name
        self.course_code=course_code
        self.enrolled_student=[]
class school:
    def __init__(self,name):
        self.name=name
        self.students=[]
        self.courses=[]
    def add_student(self,student):
        self.students.append(student)
    def add_course(self,course):
        self.courses.append(course)
    def enroll_student(self,student_id,course_code):
        student=next((s for s in self.students if s.student_id==student_id),None)
        course=next((c for c in self.courses if c.course_code==course_code),None)
        if student and course:
            course.enrolled_student.append(student)
            print(f"{student.name} enroll to {course.course_name}")
school=school("ABC school")
s1=student("dilli","1245")
c1=course("python","p001")

school.add_student(s1)
school.add_course(c1)
school.enroll_student("1245","p001")            
