from typing import Annotated, Any, List, Literal, Optional, Union

from pydantic import Field

from .base_model import BaseModel


class GetAccounts(BaseModel):
    viewer: Optional["GetAccountsViewer"]


class GetAccountsViewer(BaseModel):
    accounts: Optional[
        List[
            Optional[
                Annotated[
                    Union[
                        "GetAccountsViewerAccountsAccountInterface",
                        "GetAccountsViewerAccountsAccount",
                    ],
                    Field(discriminator="typename__"),
                ]
            ]
        ]
    ]


class GetAccountsViewerAccountsAccountInterface(BaseModel):
    typename__: Literal["AccountInterface"] = Field(alias="__typename")


class GetAccountsViewerAccountsAccount(BaseModel):
    typename__: Literal["Account"] = Field(alias="__typename")
    number: Optional[str]
    solar_wallet_available_credit: Optional[int] = Field(
        alias="solarWalletAvailableCredit"
    )
    balance: int
    properties: Optional[List[Optional["GetAccountsViewerAccountsAccountProperties"]]]


class GetAccountsViewerAccountsAccountProperties(BaseModel):
    id: Optional[str]
    electricity_supply_points: Optional[
        List[
            Optional[
                "GetAccountsViewerAccountsAccountPropertiesElectricitySupplyPoints"
            ]
        ]
    ] = Field(alias="electricitySupplyPoints")


class GetAccountsViewerAccountsAccountPropertiesElectricitySupplyPoints(BaseModel):
    active_agreement: Optional[
        "GetAccountsViewerAccountsAccountPropertiesElectricitySupplyPointsActiveAgreement"
    ] = Field(alias="activeAgreement")


class GetAccountsViewerAccountsAccountPropertiesElectricitySupplyPointsActiveAgreement(
    BaseModel
):
    details: Optional[
        "GetAccountsViewerAccountsAccountPropertiesElectricitySupplyPointsActiveAgreementDetails"
    ]
    product: Optional[
        "GetAccountsViewerAccountsAccountPropertiesElectricitySupplyPointsActiveAgreementProduct"
    ]


class GetAccountsViewerAccountsAccountPropertiesElectricitySupplyPointsActiveAgreementDetails(
    BaseModel
):
    contractual_max_power: Optional[List[Optional[Any]]] = Field(
        alias="contractualMaxPower"
    )


class GetAccountsViewerAccountsAccountPropertiesElectricitySupplyPointsActiveAgreementProduct(
    BaseModel
):
    prices: Optional[
        "GetAccountsViewerAccountsAccountPropertiesElectricitySupplyPointsActiveAgreementProductPrices"
    ]


class GetAccountsViewerAccountsAccountPropertiesElectricitySupplyPointsActiveAgreementProductPrices(
    BaseModel
):
    fixed_term: Optional[List[Optional[float]]] = Field(alias="fixedTerm")
    variable_term: Optional[List[Optional[float]]] = Field(alias="variableTerm")
    surplus_rate: Optional[float] = Field(alias="surplusRate")


GetAccounts.model_rebuild()
GetAccountsViewer.model_rebuild()
GetAccountsViewerAccountsAccount.model_rebuild()
GetAccountsViewerAccountsAccountProperties.model_rebuild()
GetAccountsViewerAccountsAccountPropertiesElectricitySupplyPoints.model_rebuild()
GetAccountsViewerAccountsAccountPropertiesElectricitySupplyPointsActiveAgreement.model_rebuild()
GetAccountsViewerAccountsAccountPropertiesElectricitySupplyPointsActiveAgreementProduct.model_rebuild()
