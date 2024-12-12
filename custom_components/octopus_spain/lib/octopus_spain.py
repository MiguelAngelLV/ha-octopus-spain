from dataclasses import dataclass

from custom_components.octopus_spain.api import (
    GetAccountsViewerAccountsAccount,
    OctopusAPI,
)


@dataclass
class OctopusAccount:
    id: str
    solar_wallet: float
    octopus_credit: float
    price_p1: float
    price_p2: float
    price_p3: float
    prices_surplus: float

def _convert_account(account: GetAccountsViewerAccountsAccount):
    prices = account.properties[0].electricity_supply_points[0].active_agreement.product.prices
    return OctopusAccount(
        id=account.number,
        solar_wallet=account.solar_wallet_available_credit/100,
        octopus_credit=account.balance/100,
        price_p1=prices.variable_term[0],
        price_p2=prices.variable_term[1],
        price_p3=prices.variable_term[2],
        prices_surplus=prices.surplus_rate
    )

class OctopusSpain:

    _URL = "https://api.oees-kraken.energy/v1/graphql/"

    def __init__(self, email, password):
        self._api = None
        self._email = email
        self._password = password
        self._token = None

    async def login(self):
        self._api = OctopusAPI(url=self._URL)
        response = await self._api.login(self._email, self._password)
        self._api = OctopusAPI(url=self._URL, headers={"authorization": response.obtain_kraken_token.token})
        return True

    async def accounts(self):
        response = await self._api.get_accounts()
        return map(_convert_account, response.viewer.accounts)
