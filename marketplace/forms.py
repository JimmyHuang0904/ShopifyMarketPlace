from flask import current_app
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import TextField, PasswordField, SelectField, TextAreaField
from wtforms import validators

from .models.user import User

db = SQLAlchemy()


class LoginForm(FlaskForm):
    username = TextField(u'Username', validators=[validators.required()])
    password = PasswordField(u'Password', validators=[validators.optional()])

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        # if our validator do not pass
        if not check_validate:
            return False

        # TODO: We could add LDAP authentication for real production
        # if current_app.config['LDAP_LOGIN']:
        #     # Check credentials against LDAP server
        #     if not ldap.bind_user(self.username.data, self.password.data):
        #         self.username.errors.append('Invalid username or password')
        #         return False
        #     else:
        #         current_app.logger.debug(
        #             "Login OK for %s" % self.username.data)

        # Does our user exists
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            user = User(username=self.username.data)
            db.session.add(user)
            db.session.commit()

        return True
