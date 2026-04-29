from sqlalchemy import func, desc
from database import Session
from models import Student, Grade, Subject, Group, Teacher


session = Session()


# 1
def select_1():
    return session.query(
        Student.name,
        func.avg(Grade.grade).label("avg_grade")
    ).join(Grade).group_by(Student.id)\
     .order_by(desc("avg_grade")).limit(5).all()


# 2
def select_2(subject_id):
    return session.query(
        Student.name,
        func.avg(Grade.grade).label("avg_grade")
    ).join(Grade).filter(
        Grade.subject_id == subject_id
    ).group_by(Student.id)\
     .order_by(desc("avg_grade")).first()


# 3
def select_3(subject_id):
    return session.query(
        Group.name,
        func.avg(Grade.grade)
    ).join(Student).join(Grade)\
     .filter(Grade.subject_id == subject_id)\
     .group_by(Group.id).all()


# 4
def select_4():
    return session.query(func.avg(Grade.grade)).scalar()


# 5
def select_5(teacher_id):
    return session.query(Subject.name)\
        .filter(Subject.teacher_id == teacher_id).all()


# 6
def select_6(group_id):
    return session.query(Student.name)\
        .filter(Student.group_id == group_id).all()


# 7
def select_7(group_id, subject_id):
    return session.query(
        Student.name,
        Grade.grade
    ).join(Grade).filter(
        Student.group_id == group_id,
        Grade.subject_id == subject_id
    ).all()


# 8
def select_8(teacher_id):
    return session.query(func.avg(Grade.grade))\
        .join(Subject)\
        .filter(Subject.teacher_id == teacher_id).scalar()


# 9
def select_9(student_id):
    return session.query(Subject.name)\
        .join(Grade)\
        .filter(Grade.student_id == student_id)\
        .distinct().all()


# 10
def select_10(student_id, teacher_id):
    return session.query(Subject.name)\
        .join(Grade)\
        .filter(
            Grade.student_id == student_id,
            Subject.teacher_id == teacher_id
        ).distinct().all()