from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, ValidationError
import re


def validate_data(self, data_field):
    p = re.compile(r'(?=.*\d)(?=.*[a-z])')
    if not p.match(data_field.data):
        raise ValidationError("Minimum 1 digit and 1 lower case letter required")


def char_check(form, field):
    excluded_char = "&<>%"

    for char in field.data:
        if char in excluded_char:
            raise ValidationError(f"Char {char} is not allowed")


class RegisterForm(FlaskForm):
    username = EmailField(validators=[DataRequired(), Email(), char_check])
    password = PasswordField(validators=[DataRequired(), Length(min=8, max=15), char_check, validate_data])
    # confirm_password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()
