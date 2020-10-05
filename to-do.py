# All imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

# create engine
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

# describe table
Base = declarative_base()

class Tasks(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return (f'{self.id}. {self.task}')

# create table 'task' in db 'todo.db'
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# method to get today's tasks
def read_today():
    # create session
    read_session = Session()
    #today_tasks = read_session.query(Tasks).filter_by(Tasks.deadline == datetime.today())
    today = datetime.today()
    today_tasks = read_session.query(Tasks).all()
    print('Today ' + today.strftime("%#d %b") + ':')
    if len(today_tasks) == 0:
        print('Nothing to do!')
    else:
        for task in today_tasks:
            print(task)
    print()
    read_session.commit()

# method to get week's tasks
def read_week():
    # create session
    read_session = Session()
    today = datetime.today()
    end_of_the_week = today + timedelta(days=6)
    week_tasks = read_session.query(Tasks).filter(Tasks.deadline <= end_of_the_week, Tasks.deadline >= today.date()).order_by(Tasks.deadline)

    for x in range(0, 7):
        current_day = today + timedelta(days=x)
        print('{}:'.format(current_day.strftime('%A %d %b')))
        count = 1
        there_was_a_task = False
        for task in week_tasks:
            if task.deadline == current_day.date():
                print('{}. {}'.format(count, task.task))
                print()
                there_was_a_task = True
                count += 1
        if there_was_a_task != True:
            print('Nothing to do!')
            print()
    read_session.commit()

def read_all():
    # create session
    read_session = Session()
    all_tasks = read_session.query(Tasks).filter().order_by(Tasks.deadline)
    print('All tasks:')
    for task in all_tasks:
            print(str(task.id) + '. ' + task.task + '. ' + task.deadline.strftime("%#d %b"))
    print()
    read_session.commit()

def read_missed():
    # create session
    read_session = Session()
    today = datetime.today()
    missed_tasks = read_session.query(Tasks).filter(Tasks.deadline < today.date()).order_by(Tasks.deadline)
    print('Missed tasks:')
    for task in missed_tasks:
            print(str(task.id) + '. ' + task.task + '. ' + task.deadline.strftime("%#d %b"))
    print()
    read_session.commit()

# method to update db
def add_task(task_name, task_deadline):
    update_session = Session()
    new_task = Tasks(task=task_name, deadline=task_deadline)
    update_session.add(new_task)
    update_session.commit()
    print('The task has been added!')

# method to update db
def delete_task():
    # create session
    update_session = Session()
    all_tasks = update_session.query(Tasks).filter().order_by(Tasks.deadline)
    todo = False
    to_delete = 0
    for task in all_tasks:
        todo = True
    if todo == False:
        print('Nothing to do!')
    else:
        print('Choose the number of the task you want to delete:')
        for task in all_tasks:
            print(str(task.id) + '. ' + task.task + '. ' + task.deadline.strftime("%#d %b"))
        to_delete = int(input())
        specific_row = all_tasks[to_delete-1]
        update_session.delete(specific_row)
    print('The task has been deleted!')
    print()
    update_session.commit()

#---- main program execution starts here----
while(True):
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")

    choice = int(input())
    if choice == 1:
        print()
        read_today()
    elif choice == 2:
        print()
        read_week()
    elif choice == 3:
        print()
        read_all()
    elif choice == 4:
        print()
        read_missed()
    elif choice == 5:
        print('Enter task')
        task_name = input()
        print('Enter deadline')
        deadline_str = input()
        deadline_format = datetime.strptime(deadline_str, "%Y-%m-%d")
        add_task(task_name,task_deadline=datetime.date(deadline_format))
    elif choice == 6:
        print()
        delete_task()
    elif choice == 0:
        print()
        print('Bye!')
        break
