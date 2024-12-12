from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetSolar(BaseModel):
    account: Optional["GetSolarAccount"]


class GetSolarAccount(BaseModel):
    solar_wallet_available_credit: Optional[int] = Field(
        alias="solarWalletAvailableCredit"
    )


GetSolar.model_rebuild()
