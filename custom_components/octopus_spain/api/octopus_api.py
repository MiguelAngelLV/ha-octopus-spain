from typing import Any, Dict

from .async_base_client import AsyncBaseClient
from .get_accounts import GetAccounts
from .login import Login


def gql(q: str) -> str:
    return q


class OctopusAPI(AsyncBaseClient):
    async def get_accounts(self, **kwargs: Any) -> GetAccounts:
        query = gql(
            """
            query GetAccounts {
              viewer {
                accounts {
                  __typename
                  ... on Account {
                    number
                    solarWalletAvailableCredit
                    balance
                    properties {
                      id
                      electricitySupplyPoints {
                        activeAgreement {
                          details {
                            contractualMaxPower
                          }
                          product {
                            prices {
                              fixedTerm
                              variableTerm
                              surplusRate
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query, operation_name="GetAccounts", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetAccounts.model_validate(data)

    async def login(self, email: str, password: str, **kwargs: Any) -> Login:
        query = gql(
            """
            mutation Login($email: String!, $password: String!) {
              obtainKrakenToken(input: {email: $email, password: $password}) {
                token
              }
            }
            """
        )
        variables: Dict[str, object] = {"email": email, "password": password}
        response = await self.execute(
            query=query, operation_name="Login", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return Login.model_validate(data)
