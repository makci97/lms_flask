from app.project import db, USER_MODEL_CLASS
from app.project.value_objects.education_info import EducationDegree, EducationForm, EducationBasis


class Student(USER_MODEL_CLASS):
    """ Student Model for storing student related details """
    __tablename__ = "student"

    study_group_id = db.Column(db.Integer, db.ForeignKey('study_group.id'), nullable=False)
    entrance_year = db.Column(db.Integer, nullable=True, default=None)
    education_degree = db.Column(db.Enum(EducationDegree), nullable=False, default=EducationDegree.nan)
    education_form = db.Column(db.Enum(EducationForm), nullable=False, default=EducationForm.nan)
    education_basis = db.Column(db.Enum(EducationBasis), nullable=False, default=EducationBasis.nan)

    def __repr__(self):
        return f'Student {self.name} {self.surname}'
