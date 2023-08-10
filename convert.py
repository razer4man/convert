from typing import List

import requests

from utils import CURRENCIES_ID


def get_currencies_course(url: str) -> List[dict[str, str]]:
    try:
        response = requests.get(url)
        currencies = response.json()
        return currencies
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending the request: {e}")
        return []


def convert_amount(value: float, url: str) -> List[str]:
    """Return a list of converted amount currencies."""
    converted_amount: List[str] = []
    currencies = get_currencies_course(url)

    for i in CURRENCIES_ID:
        for j in currencies:
            if i == j["Cur_ID"]:
                converted_value = round(
                    value / (j["Cur_OfficialRate"]) * j["Cur_Scale"], 2
                )
                converted_amount.append(f"{converted_value} {j['Cur_Abbreviation']}")
    return converted_amount
