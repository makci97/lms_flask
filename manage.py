import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.project import create_app, db
from app.project.user.user_model import User
from app.project.student.student_model import Student
from app.project.teacher.teacher_model import Teacher
from app.project.study_group.study_group_model import StudyGroup
from app.project.study_course.study_course_model import StudyCourse
from app.project.courses_and_groups.courses_and_groups_model import CoursesAndGroups
from app.project.courses_and_teachers.courses_and_teachers_model import CoursesAndTeachers

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()

