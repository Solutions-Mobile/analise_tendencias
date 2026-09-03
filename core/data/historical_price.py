from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass(frozen=True)
class HistoricalPrice:
    asset_id: UUID
    date: date

    open: float
    high: float
    low: float
    close: float
    average: float

    trades: int
    quantity: int
    volume: float
    