import argparse
from models import Session, Teacher

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--action", choices=["create", "list", "update", "remove"])
parser.add_argument("-m", "--model", choices=["Teacher"])
parser.add_argument("--id", type=int)
parser.add_argument("--name", type=str)

args = parser.parse_args()
session = Session()

if args.model == "Teacher":
    if args.action == "create":
        teacher = Teacher(name=args.name)
        session.add(teacher)
        session.commit()
        print(f"Created teacher {args.name}")
    elif args.action == "list":
        print(session.query(Teacher).all())
    elif args.action == "update":
        teacher = session.query(Teacher).get(args.id)
        teacher.name = args.name
        session.commit()
    elif args.action == "remove":
        teacher = session.query(Teacher).get(args.id)
        session.delete(teacher)
        session.commit() 