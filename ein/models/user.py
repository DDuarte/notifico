#!/usr/bin/env python
# encoding: utf-8
import datetime

from werkzeug import security

from ein.server import db


class User(db.Model):
    __tablename__ = 'users'

    #: The unique, auto-incrementing identifier for a user.
    id = db.Column(db.Integer, primary_key=True)

    #: The user's default email address. Also used as the login
    #: username for new-style accounts.
    primary_email = db.Column(db.String(255), nullable=False)

    #: The user's (hashed) password.
    password = db.Column(db.String(255), nullable=False)

    #: UTC timestamp of the user's registration date.
    joined = db.Column(db.TIMESTAMP(), default=datetime.datetime.utcnow)

    #: Legacy usernames imported from Notifico, the predecessor to Ein.
    legacy_username = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, primary_email, password):
        self.primary_email = primary_email
        self.change_password(password)

    def change_password(self, new_password):
        """
        Change the user's password.

        :param new_password: The new user password.

        .. note::

            Explicitly commits the current database session.
        """
        # Hash and salt the password using PBKDF2/SHA1/HMAC with 12 rounds.
        # Although this is the default, it's specified explicitly in the case
        # of the default changing in the future.
        self.password = security.generate_password_hash(
            new_password,
            method='pbkdf2:sha1:12',
            salt_length=8
        )

        # Explicitly commits the current transaction.
        db.session.add(self)
        db.session.commit()

    def check_password(self, password):
        """
        Checks to see if a plain-text password matche the hashed and salted
        password stored in the database.

        :param password: The plain-text password to compare.
        :returns: True if valid, False otherwise.
        :rtype: bool
        """
        return security.check_password_hash(self.password, password)
