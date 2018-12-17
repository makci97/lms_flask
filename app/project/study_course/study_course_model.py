from app.project import db


class StudyCourse(db.Model):
    """ StudyCourse Model for storing study course related details """
    __tablename__ = "study_course"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), nullable=False, unique=True)

    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(100), nullable=True)

    teachers = db.relationship(
        'Teacher', secondary='courses_and_teachers', backref=db.backref('teachers', lazy='dynamic'), lazy='subquery'
    )
    groups = db.relationship(
        'StudyGroup', secondary='courses_and_groups', backref=db.backref('groups', lazy='dynamic'), lazy='subquery'
    )

    def __repr__(self):
        return f'StudyCourse {self.name}'
