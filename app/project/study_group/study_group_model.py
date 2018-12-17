from app.project import db


class StudyGroup(db.Model):
    """ StudyGroup Model for storing groups of students related details """
    __tablename__ = "study_group"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), nullable=False, unique=True)

    n_course = db.Column(db.Integer, nullable=False, default=1)
    group_name = db.Column(db.String(64), nullable=False, unique=True)
    faculty_name = db.Column(db.String(64), nullable=False)

    students = db.relationship('student', backref='study_group', lazy='dynamic')

    def __repr__(self):
        return f'StudyGroup {self.group_name}'
