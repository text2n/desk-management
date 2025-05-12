from fastapi.templating import Jinja2Templates
from pydantic import (
    MySQLDsn,
    computed_field,
)
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # Use top level .env file (one level above ./backend/)
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )
    db_host: str = '127.0.0.1'
    db_port: int = 3306
    db_user: str = "root"
    db_password: str = "Admin@123"
    db_name: str = ""
    DEBUG: int = 0
    GOOGLE_API_KEY: str = ""
    @computed_field  # type: ignore[prop-decorator]
    @property
    def DATABASE_URI(self) -> MySQLDsn:
        return str(MultiHostUrl.build(
            scheme="mysql+mysqlconnector",
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            path=self.db_name,
        ))

settings = Settings()  # type: ignore
