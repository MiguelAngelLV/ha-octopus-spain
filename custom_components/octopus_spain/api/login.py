from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class Login(BaseModel):
    obtain_kraken_token: Optional["LoginObtainKrakenToken"] = Field(
        alias="obtainKrakenToken"
    )


class LoginObtainKrakenToken(BaseModel):
    token: str


Login.model_rebuild()
