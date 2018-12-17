import enum


class EducationDegree(enum.Enum):
    nan = 0
    bachelor = 1
    specialist = 2
    master = 3


class EducationForm(enum.Enum):
    nan = 0
    full_time = 1
    distance = 2
    evening = 3


class EducationBasis(enum.Enum):
    nan = 0
    budget = 1
    contract = 2
