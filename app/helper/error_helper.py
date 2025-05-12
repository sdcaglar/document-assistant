from enum import IntEnum
from gettext import gettext as _


class ErrorCode(IntEnum):
    def __new__(cls, value, phrase, message=""):
        obj = int.__new__(cls, value)
        obj._value_ = value

        obj.phrase = phrase
        obj.message = message
        return obj

    deactivate_user = 10000, _("Hesabınız geçici olarak kapatıldı.")
    invalid_login = 10001, _("Hatalı e-mail veya şifre.")
    email_already_exists = 10002, _("Sistemde kayıtlı e-posta adresi bulunmakta")
    user_not_found = 10003, _("Kullanıcı bulunamadı")


errors = ErrorCode
