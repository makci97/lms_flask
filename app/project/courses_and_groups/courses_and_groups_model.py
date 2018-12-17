from app.project import db


class CoursesAndGroups(db.Model):
    """ CoursesAndGroups Model for storing relations between study courses and study groups """
    __tablename__ = "courses_and_groups"

    course_id = db.Column(db.Integer, db.ForeignKey('study_course.id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('study_group.id'), primary_key=True)
