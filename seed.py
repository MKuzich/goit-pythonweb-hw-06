from faker import Faker
from models import Session, Group, Student, Teacher, Subject, Grade
import random

fake = Faker()
session = Session()

groups = [Group(name=f"Group-{i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()

teachers = [Teacher(name=fake.name()) for _ in range(4)]
session.add_all(teachers)
session.commit()

subjects = [Subject(name=fake.word(), teacher=random.choice(teachers)) for _ in range(6)]
session.add_all(subjects)
session.commit()

students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(40)]
session.add_all(students)
session.commit()

for student in students:
    for subject in subjects:
        for _ in range(random.randint(10, 20)):
            session.add(Grade(student=student, subject=subject, grade=random.randint(1, 100)))

session.commit()
session.close()