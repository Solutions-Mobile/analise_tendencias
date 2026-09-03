#core\data\market_data.py

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class MarketData:
    date: date
    symbol: str
    market_type: int
    bdi_code: int

    name: str
    specification: str
    currency: str
    isin: str

    open: float
    high: float
    low: float
    average: float
    close: float
    bid: float
    ask: float

    trades: int
    quantity: int
    volume: float

    quotation_factor: int

    exercise_price: float
    exercise_indicator: int
    expiration_date: Optional[date]
    exercise_points: float
    distribution_number: int
