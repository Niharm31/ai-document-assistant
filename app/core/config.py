from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "AI Document Assistant"
    app_env: str = "production"
    database_url: str = "sqlite:///./data/documents.db"
    upload_dir: str = "./data/documents"
    vector_dir: str = "./data/vector_store"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    top_k: int = 5
    max_upload_mb: int = 20

    # Any OpenAI-compatible chat-completions endpoint.
    llm_base_url: str = "http://127.0.0.1:8080/v1"
    llm_api_key: str = "local"
    llm_model: str = "local-model"

    # Comma-separated browser origins. "*" is convenient for local testing,
    # but use explicit origins for a public deployment.
    cors_origins: str = "*"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def cors_origin_list(self) -> list[str]:
        if self.cors_origins.strip() == "*":
            return ["*"]
        return [x.strip() for x in self.cors_origins.split(",") if x.strip()]

settings = Settings()
