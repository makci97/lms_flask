from app.project import db, USER_MODEL_CLASS


class Teacher(USER_MODEL_CLASS):
    """ Teacher Model for storing teacher related details """
    __tablename__ = "teacher"

    study_courses = db.relationship(
        'StudyCourse', secondary='courses_and_teachers',
        backref=db.backref('study_courses', lazy='dynamic'), lazy='subquery'
    )

    def __repr__(self):
        return f'Teacher {self.name} {self.surname}'
