#core\data\b3_raw_record.py
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class B3RawRecord:
    date: Optional[date]

    bdi_code: int
    symbol: str
    market_type: int
    name: str
    specification: str
    currency: str

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

    exercise_price: float
    exercise_indicator: int
    expiration_date: Optional[date]

    quotation_factor: int
    exercise_points: float

    isin: str
    distribution_number: int
    