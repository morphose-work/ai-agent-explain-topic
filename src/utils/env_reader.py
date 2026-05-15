from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class ENV_READER(BaseSettings):
    OPENROUTER_MODEL: str
    OPENROUTER_API_KEY: SecretStr
    OPENROUTER_BASE_URL: str

    model_config = SettingsConfigDict(
        env_file='.env'
    )

    def get_api_key(self) -> str:
        return self.OPENROUTER_API_KEY.get_secret_value()