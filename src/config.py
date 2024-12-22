"""Configuration settings."""

from pydantic import BaseSettings


class Config(BaseSettings):
    """Configuration class using Pydantic."""

    DEFAULT_SEPARATOR: str = ","
