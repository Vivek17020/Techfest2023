from uagents import Model
from typing import Dict, List, Tuple

class UserSettings(Model):
    """
    Represents user settings for currency exchange monitoring.

    Attributes:
        base_currency (str): The user's base currency.
        foreign_currencies (List[str]): List of foreign currencies to monitor.
        alert_thresholds (Dict[str, Tuple[float, float]]): Alert thresholds for each foreign currency.
    """

    base_currency: str
    foreign_currencies: List[str]
    alert_thresholds: Dict[str, Tuple[float, float]]

class ExchangeRateUpdate(Model):
    """
    Represents an update of exchange rates.

    Attributes:
        base_currency (str): The base currency for the exchange rates.
        rates (Dict[str, float]): Exchange rates for foreign currencies.
    """

    base_currency: str
    rates: Dict[str, float]