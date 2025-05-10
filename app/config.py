from app.base_config import DefaultSettings


class DevelopmentConfig(DefaultSettings):
    def __init__(self):
        super().__init__()


settings = DevelopmentConfig()

try:
    from app.user_config import user_settings

    settings = DevelopmentConfig()
    for k in user_settings.__dict__:
        settings.__dict__[k] = user_settings.__dict__[k]
except ImportError:
    pass
