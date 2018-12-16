from app.project import db, flask_bcrypt


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))
    verification_code = db.Column(db.String(16), nullable=False, unique=True)

    name = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=False)
    middle_name = db.Column(db.String(64), nullable=True, default=None)

    email = db.Column(db.String(120), nullable=False, unique=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.name} {self.surname}'
