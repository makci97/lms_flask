from app.project import db


class CoursesAndTeachers(db.Model):
    """ CoursesAndTeachers Model for storing relations between study courses and teachers """
    __tablename__ = "courses_and_teachers"

    course_id = db.Column(db.Integer, db.ForeignKey('study_course.id'), primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), primary_key=True)
