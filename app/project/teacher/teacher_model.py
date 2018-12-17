from app.project import USER_MODEL_CLASS


class Teacher(USER_MODEL_CLASS):
    """ Teacher Model for storing teacher related details """
    __tablename__ = "teacher"

    # study_course: StudyCourse

    def __repr__(self):
        return f'Teacher {self.name} {self.surname}'