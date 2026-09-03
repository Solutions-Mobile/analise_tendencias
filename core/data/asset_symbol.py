#core\data\asset_symbol.py

from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass(frozen=True)
class AssetSymbol:
    asset_id: UUID
    symbol: str
    valid_from: date
    valid_to: date | None
    