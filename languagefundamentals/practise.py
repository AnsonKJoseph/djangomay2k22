class Course:
    def post(self, **kwargs):
        self.course_name = kwargs.get("course_name")
        self.active_status = kwargs.get("active_status")

    def __str__(self):
        return self.course_name


class Batch:
    def post(self, **kwargs):
        self.course = kwargs.get("course")
        self.batch_code = kwargs.get("batch_code")
        self.start_date = kwargs.get("start_date")

    def __str__(self):
        return self.batch_code


class Student:
    def post(self, **kwargs):
        self.student_name = kwargs.get("student_name")
        self.phone = kwargs.get("phone")
        self.batch = kwargs.get("batch")

    def __str__(self):
        return self.student_name


django = Course()
django.post(course_name="django", active_status="active")

mearn = Course()
mearn.post(course_name="mearn", active_status="active")

dj1 = Batch()
dj1.post(course=django, batch_code="5687", start_date="2-06-2022")

mn1 = Batch()
mn1.post(course=mearn, batch_code="098", start_date="6-07-2022")

rahul = Student()
rahul.post(student_name="rahul", phone="123456789", batch=mn1)

print(rahul.batch.course)

print(rahul)
