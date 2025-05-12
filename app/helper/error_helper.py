from enum import IntEnum
from gettext import gettext as _


class ErrorCode(IntEnum):
    def __new__(cls, value, phrase, message=""):
        obj = int.__new__(cls, value)
        obj._value_ = value

        obj.phrase = phrase
        obj.message = message
        return obj

    deactivate_user = 10000, _("Your account has been temporarily deactivated.")
    invalid_login = 10001, _("Incorrect email or password.")
    email_already_exists = (
        10002,
        _("The email address is already registered in the system."),
    )
    user_not_found = 10003, _("User not found.")
    unsupported_data_type = 10004, _("Unsupported data type.s")
    invalid_access_session = (
        10005,
        _("Session expired due to inactivity. Please log in again."),
    )
    disabled_session = (
        10006,
        _("Session terminated due to new login from another device."),
    )
    invalid_access_token = 10007, _("Invalid access token.")


errors = ErrorCode
