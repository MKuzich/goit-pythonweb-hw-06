from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Student, Grade, Teacher, Subject, Group 
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

def select_1():
    session = get_session() 
    result = session.query(
        Student.id,
        Student.name,
        func.avg(Grade.grade).label('average_grade')
    ).join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
    session.close()
    return result

def select_2(subject_id):
    session = get_session()
    result = session.query(
        Student.id,
        Student.name,
        func.avg(Grade.grade).label('average_grade')
    ).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).first()
    session.close()
    return result

def select_3(subject_id):
    session = get_session()
    result = session.query(
        Group.name,
        func.avg(Grade.grade).label('average_grade')
    ).select_from(Group).join(Student).join(Grade).filter(Grade.subject_id == subject_id) \
        .group_by(Group.id).all()
    session.close()
    return result


def select_4():
    session = get_session()
    result = session.query(
        func.avg(Grade.grade).label('overall_average')
    ).all()
    session.close()
    return result

def select_5(teacher_id):
    session = get_session()
    result = session.query(
        Subject.name
    ).join(Teacher).filter(Subject.teacher_id == teacher_id).all()
    session.close()
    return result

def select_6(group_id):
    session = get_session()
    result = session.query(
        Student.id,
        Student.name
    ).join(Group).filter(Group.id == group_id).all()
    session.close()
    return result

def select_7(group_id, subject_id):
    session = get_session()
    result = session.query(
        Student.name,
        Grade.grade,
        Grade.date_received
    ).join(Group).join(Grade).filter(Group.id == group_id, Grade.subject_id == subject_id).all()
    session.close()
    return result

def select_8(teacher_id):
    session = get_session()
    result = session.query(
        func.avg(Grade.grade).label('average_grade')
    ).join(Subject).join(Teacher).filter(Teacher.id == teacher_id).all()
    session.close()
    return result

def select_9(student_id):
    session = get_session()
    result = session.query(
        Subject.name
    ).join(Grade).filter(Grade.student_id == student_id).all()
    session.close()
    return result

def select_10(student_id, teacher_id):
    session = get_session()
    result = session.query(
        Subject.name
    ).join(Grade).join(Teacher).filter(Grade.student_id == student_id, Teacher.id == teacher_id).all()
    session.close()
    return result

if __name__ == "__main__":
    print(select_1())
    print(select_2(1))
    print(select_3(1))
    print(select_4())
    print(select_5(1))
    print(select_6(1))
    print(select_7(1, 1))
    print(select_8(1))
    print(select_9(1))
    print(select_10(1, 1))
