from faker import Faker
from random import randint, choice
from database import Session
from models import Group, Student, Teacher, Subject, Grade

fake = Faker()
session = Session()

session.query(Grade).delete()
session.query(Student).delete()
session.query(Subject).delete()
session.query(Teacher).delete()
session.query(Group).delete()
session.commit()

# --------------------
# GROUPS
# --------------------
groups = [Group(name=f"Group-{i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()

# --------------------
# TEACHERS
# --------------------
teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

# --------------------
# SUBJECTS
# --------------------
subjects = []
for i in range(1, 7):
    subject = Subject(
        name=f"Subject-{i}",
        teacher=choice(teachers)
    )
    subjects.append(subject)

session.add_all(subjects)
session.commit()

# --------------------
# STUDENTS
# --------------------
students = []
for _ in range(40):
    student = Student(
        name=fake.name(),
        group=choice(groups)
    )
    students.append(student)

session.add_all(students)
session.commit()

# --------------------
# GRADES
# --------------------
for student in students:
    for _ in range(randint(10, 20)):
        grade = Grade(
            grade=randint(60, 100),
            student=student,
            subject=choice(subjects),
            created_at=fake.date_time_this_year()
        )
        session.add(grade)

session.commit()
session.close()

print("Database seeded successfully!")