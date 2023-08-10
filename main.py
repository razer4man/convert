from convert import convert_amount


from user_input import amount


from utils import URL_GET_CURRENCIES
import requests


def main() -> str:
    """Get user's amount, currencies from API and then convert amount to different currencies."""
    convert_amount_string = convert_amount(amount, URL_GET_CURRENCIES)
    return "; ".join(convert_amount_string)


if __name__ == "__main__":
    print(main())
