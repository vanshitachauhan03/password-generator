import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DEBUG = True

    # API settings
    DEFAULT_PASSWORD_LENGTH = 16
    MAX_PASSWORD_LENGTH = 64