import os

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BaseConfig(BaseSettings):
    username: str
    password: str
    base_url: str
    after_login_url: str

    data_dir: str = os.path.join(BASE_DIR, "data/")

    @property
    def credentials_file(self):
        return os.path.join(self.data_dir, "credentials.json")

    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"), env_file_encoding="utf-8"
    )


settings = BaseConfig()
